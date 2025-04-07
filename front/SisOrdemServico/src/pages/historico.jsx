import React, { useState, useEffect } from "react";
import axios from "axios";

export function Historico() {
  const [dados, setDados] = useState([]);
  const token = localStorage.getItem('token');

  useEffect(() => {
    if (!token) return;

    const fetchData = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/ordemServico", {
          headers: { Authorization: `Bearer ${token}` },
        });
        setDados(response.data);
        console.log(response.data);
      } catch (error) {
        console.error("Erro ao buscar dados:", error);
      }
    };
    fetchData();
  }, [token]);

  return (
    <div className="bg-gray-50 flex flex-col items-center w-full py-12 px-4">
      <h1 className="text-3xl font-bold text-gray-800 mb-8">Histórico</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-3 w-[1100px]">
        {dados.map((historico) => (
          <div key={historico.id} className="bg-white shadow-md rounded-xl p-4 flex justify-between items-center hover:shadow-lg transition-all">
            <div>
              <p className="text-sm text-gray-500">ID #{historico.id}</p>
              <p className="text-lg font-semibold text-gray-800">{historico.descricao_manutencao}</p>
            </div>
            <div className="text-[#007bc0]">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none"
                viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2"
                  d="M4 6h16M4 10h16M4 14h16M4 18h16" />
              </svg>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
