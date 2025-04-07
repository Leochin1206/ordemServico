import { Link } from "react-router-dom";
import { useState } from "react";
import iconNav from "../assets/order.svg";
import logout from "../assets/logout.svg"

export function Navbar() {
    const [isOpen, setIsOpen] = useState(false);

    const handleLinkClick = () => {
        setIsOpen(false);
    };

    const handleLogout = () => {
        // Remove os tokens do localStorage
        localStorage.removeItem("access");
        localStorage.removeItem("refresh");

        // Redireciona para a tela de login
        window.location.href = "/";
    };

    return (
        <nav className="p-4 flex justify-between items-center relative shadow-lg">
            <div className="flex items-center">
                <img src={iconNav} alt="Logo" className="w-[40px] h-auto" />

                <div className=" relative">
                    <button onClick={() => setIsOpen(!isOpen)} className="bg-white text-[#007bc0] px-4 py-2">
                        <svg className="w-4 h-4 transform transition group-hover:rotate-180"
                            fill="none" stroke="currentColor"
                            strokeWidth="2"
                            viewBox="0 0 24 24">
                            <path d="M19 9l-7 7-7-7" />
                        </svg>
                    </button>

                    {isOpen && (
                        <div className="absolute top-full left-0 bg-white text-black mt-1 shadow-lg rounded-md w-48 flex flex-col">
                            <Link to='/Home' className="hover:bg-gray-100 px-4 py-2" onClick={handleLinkClick}>Home</Link>
                            <Link to='/OrdemServico' className="hover:bg-gray-100 px-4 py-2" onClick={handleLinkClick}>Ordens de Serviço</Link>
                            <Link to='/Ambientes' className="hover:bg-gray-100 px-4 py-2" onClick={handleLinkClick}>Ambientes</Link>
                            <Link to='/Gestores' className="hover:bg-gray-100 px-4 py-2" onClick={handleLinkClick}>Gestores</Link>
                            <Link to='/Manutentores' className="hover:bg-gray-100 px-4 py-2" onClick={handleLinkClick}>Manutentores</Link>
                            <Link to='/Patrimonios' className="hover:bg-gray-100 px-4 py-2" onClick={handleLinkClick}>Patrimônios</Link>
                            <Link to='/Responsaveis' className="hover:bg-gray-100 px-4 py-2" onClick={handleLinkClick}>Responsáveis</Link>
                            <Link to='/Historico' className="hover:bg-gray-100 px-4 py-2" onClick={handleLinkClick}>Histórico</Link>
                        </div>
                    )}
                </div>
            </div>

            <button onClick={handleLogout}><img src={logout} className="w-[40px] h-auto" /></button>
        </nav>
    );
}
