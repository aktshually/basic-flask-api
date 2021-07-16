import { Link } from "react-router-dom";
import "./Home.scss";
import "../../assets/global/global.scss";

const HomePage = () => {

    return (
        <div id="HomePage">
            <header>
                <p>
                    Let Me Try
                </p>
                <nav>
                    <ul>
                        <li>
                            <Link to="/login">Login</Link>
                        </li>
                        <li>
                            <Link to="/register">Register</Link>
                        </li>
                    </ul>
                </nav>
            </header>

            <main>
                <span id="title">
                    Let Me Try - a new concept
                </span>
                <p>
                    Make <Link to="/login">login</Link> to find more
                </p>
            </main>
        </div>
    );

};

export default HomePage;