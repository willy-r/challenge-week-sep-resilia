import resiliaLogo from "../../assets/images/resilia-logo.png";

import "./styles.css";

function Header() {
  return (
    <header className="main-header">
      <a href="/">
        <img src={resiliaLogo} alt="Resilia logo" />
      </a>
    </header>
  );
}

export default Header;
