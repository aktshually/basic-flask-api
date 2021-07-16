import { useState } from "react";
import { ChangeEvent } from "react";
import { FormEvent } from "react";
import { Link } from "react-router-dom";

import { toast, ToastContainer, ToastOptions } from "react-toastify";

import "react-toastify/dist/ReactToastify.css";
import "./Login.scss";
import "../../assets/global/global.scss"

import axios from "axios";

const LoginPage = () => {

    const [getUserName, setUserName] = useState("");
    const [getPassword, setPassword] = useState("");

    const [user, setUser] = useState("");

    const options: ToastOptions = {
        autoClose: 3000
    };

    async function onLoginFormSubmit(event: FormEvent) {
        event.preventDefault();

        if (getUserName.trim() === "" || getPassword.trim() === "") {
            return toast.error("Você tem que preencher alguns campos!", options);
        }

        const request = await axios.get(`http://127.0.0.1:5000/login?username=${getUserName}&password=${getPassword}`);
        if (request.data.status === "logged sucessfully") {
            console.log("logged in");
        }
        else {
            return toast.error("Usuário ou senha estão incorretos!", options)
        }

    }

    function userNameOnChange(event: ChangeEvent<HTMLInputElement>) {
        setUserName(event.target.value);
    }
    function passwordOnChange(event: ChangeEvent<HTMLInputElement>) {
        setPassword(event.target.value);
    }

    return (
        <div id="LoginPage">

            <div id="left-side">
                <p id="greet">
                    Bem vindo de volta!
                </p>
                <p id="register">
                    Ainda não tem uma conta? <Link to="/register">Registre-se!</Link>
                </p>
            </div>
            <div id="login-area">
                <form onSubmit={onLoginFormSubmit}>
                    <p>
                        Log in
                    </p>

                    <input type="text" name="username" id="username" placeholder="Nome de usuário" onChange={userNameOnChange} value={getUserName}/>
                    <input type="text" name="password" id="password" placeholder="Senha" onChange={passwordOnChange} value={getPassword}/>

                    <button type="submit">
                        Log in
                    </button>
                </form>
            </div>
            <ToastContainer />

        </div>
    );

};

export default LoginPage;