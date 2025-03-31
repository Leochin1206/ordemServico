import { Link } from "react-router-dom";
import iconNav from "../assets/activity.svg";

export function Navbar() {
    return (
        <nav className="bg-amber-300 text-[#03045e] p-4 flex items-center">
            <img src={iconNav} alt="Logo" />

            <div className="relative group !ml-4">
                <div className="flex items-center gap-2 cursor-pointer">
                    <span>Páginas</span>
                    <svg className="w-4 h-4 transform transition group-hover:rotate-180" fill="none" stroke="currentColor" strokeWidth="2" viewBox="0 0 24 24">
                        <path d="M19 9l-7 7-7-7" />
                    </svg>
                </div>

                <div className="absolute hidden group-hover:flex flex-col bg-white text-black !mt-2 rounded shadow-lg w-46 z-10">
                    <Link to='/Ambientes' className="px-4 py-2 hover:bg-gray-100">Ambientes</Link>
                    <Link to='/Historico' className="px-4 py-2 hover:bg-gray-100">Histórico</Link>
                    <Link to='/' className="px-4 py-2 hover:bg-gray-100">Home</Link>
                    <Link to='/Manutentores' className="px-4 py-2 hover:bg-gray-100">Manutentores</Link>
                    <Link to='/OrdemServico' className="px-4 py-2 hover:bg-gray-100">Ordens de Serviço</Link>
                    <Link to='/Patrimonios' className="px-4 py-2 hover:bg-gray-100">Patrimônios</Link>
                    <Link to='/Responsaveis' className="px-4 py-2 hover:bg-gray-100">Responsáveis</Link>
                </div>
            </div>
        </nav>
    );
}
