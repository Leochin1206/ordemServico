import { Link } from "react-router-dom";

export function Home() {
    const paginas = [
        {
            titulo: "Ordem de Serviço",
            link: "/OrdemServico"
        },
        {
            titulo: "Ambientes",
            link: "/Ambientes"
        },
        {
            titulo: "Gestores",
            link: "/Gestores"
        },
        {
            titulo: "Manutentores",
            link: "/Manutentores"
        },
        {
            titulo: "Patrimônios",
            link: "/Patrimonios"
        },
        {
            titulo: "Responsáveis",
            link: "/Responsaveis"
        },
        {
            titulo: "Histórico",
            link: "/Historico"
        },
    ];

    return(
        <div className="flex items-center justify-center w-full h-full">
            <div className="flex flex-wrap items-center justify-center w-[70%] h-[700px] !mt-12 shadow-lg">
                {paginas.map((pag, index) => (
                    <div key={index} className="flex items-center justify-center w-[43%]">
                        <Link to={pag.link}>
                            <div className="flex items-center justify-center w-[280px] shadow-lg text-white bg-[#03045e] border-3 border-[#03045e] hover:bg-white hover:text-[#03045e] transition-all duration-300 hover:scale-110">
                                <h2 className="text-[24px] !p-3">{pag.titulo}</h2>
                            </div>
                        </Link>
                    </div>
                ))}
            </div>
        </div>
    );
}