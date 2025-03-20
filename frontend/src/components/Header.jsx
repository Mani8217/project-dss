import "./Header.scss";  
import cover from "../assets/videos/cover.mp4"


const Header = () => {
  return (
    <div className="video-container">
      <video autoPlay loop muted playsInline>
        <source src={cover} type="video/mp4" />
      </video>
    </div>
  );
};

export default Header;
