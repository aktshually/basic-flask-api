import { ChangeEvent, FormEvent, useState } from "react";
import { Link } from "react-router-dom";

import { toast, ToastContainer, ToastOptions } from "react-toastify";

import "../../assets/global/global.scss";
import "./Register.scss";

import axios from "axios"

const RegisterPage = () => {

    const [getUsername, setUsername] = useState("");
    const [getPassword, setPassword] = useState("");
    const [getEmail, setEmail] = useState("");

    const options: ToastOptions = {
        autoClose: 3000
    };

    const checkEmail = /^[\w-.]+@([\w-]+\.)+[\w-]{2,4}$/g;

    async function onRegisterFormSubmit(event: FormEvent) {
        event.preventDefault();

        if (getUsername.trim() === "" || getPassword.trim() === "" || getEmail.trim() === "") {
            return toast.error("Você precisa preencher alguns campos!", options);
        }
        if (getPassword.length < 6) {
            return toast.error("Sua senha precisa ter ao menos 6 caracteres!", options);
        }
        if (getUsername.length < 5) {
            return toast.error("Seu nome de usuário precisa ter ao menos 5 caracteres!", options);
        }
        if (checkEmail.exec(getEmail) === null) {
            return toast.error("Insira um email válido!", options);
        }

        const request = await axios.post(`http://127.0.0.1:5000/register?username=${getUsername}&password=${getPassword}&email=${getEmail}`)
        if (request.data.operation_status === "success") {
            return console.log(request.data.user_data)
        }
    }

    function emailOnChange(event: ChangeEvent<HTMLInputElement>) {
        setEmail(event.target.value);
    }

    function usernameOnChange(event: ChangeEvent<HTMLInputElement>) {
        setUsername(event.target.value);
    }

    function passwordOnChange(event: ChangeEvent<HTMLInputElement>) {
        setPassword(event.target.value);
    }

    return (

        <div id="RegisterPage">
            <div id="register-side">
                <form onSubmit={onRegisterFormSubmit}>
                    <p>
                        Registre-se
                    </p>

                    <input type="text" name="username" id="username" placeholder="Nome de usuário" onChange={usernameOnChange} value={getUsername} />
                    <input type="text" name="password" id="password" placeholder="Senha" onChange={passwordOnChange} value={getPassword} />
                    <input type="text" name="email" id="email" placeholder="Email" onChange={emailOnChange} value={getEmail} />

                    <button type="submit">
                        Registrar
                    </button>
                </form>
            </div>
            <div id="right-side">
                <p id="greet">
                    algum texto
                </p>
                <p id="login">
                    Já tem uma conta? Faça <Link to="/login">login</Link>!
                </p>
            </div>
            <ToastContainer />
        </div>

    );

};

export default RegisterPage;