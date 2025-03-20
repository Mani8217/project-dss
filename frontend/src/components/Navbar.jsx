import { Link } from "react-router-dom"
import "./Navbar.scss"

const Navbar = () => {

    return (
        <div className="navbar-container">
        
          <nav className="nav-content">
            <Link to="/" >Home</Link>
            <Link to="/about">About</Link>
            <Link to="contacts">Contacts</Link>
            <Link to="/gallery">Gallery</Link>
          </nav>
        
        </div>
    )
}
export default Navbar;