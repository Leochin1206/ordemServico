import React, { useState, useEffect } from "react";
import axios from "axios";
import addIcon from "../assets/add.svg";
import searchIcon from "../assets/search.svg";
import menuIcon from "../assets/menu.svg";
import { ModalAdd } from "../components/modalAdd";
import { ModalSearch } from "../components/modalSearch";
import { ModalDeleteEdit } from "../components/modalDeleteEdit";

export function Responsaveis() {
  const [dados, setDados] = useState([]);
  const [modalAdd, setModalAdd] = useState(false);
  const [modalSearch, setModalSearch] = useState(false);
  const [modalDeleteEdit, setModalDeleteEdit] = useState(false);
  const [responsaveisSelecionado, setResponsaveisSelecionado] = useState(null);

  const token = localStorage.getItem('token');

  useEffect(() => {
    if (!token) return;

    const fetchData = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/responsaveis", {
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
    <div className="bg-gray-50 flex flex-col items-center w-full py-12">
      <h1 className="text-3xl font-bold text-gray-800 mb-8">Responsáveis</h1>

      <div className="flex items-center justify-end gap-2 mb-4 w-[57.5%] h-auto">
        <img src={addIcon} className="bg-white shadow-md rounded-xl p-2 hover:shadow-lg transition-all" onClick={() => setModalAdd(true)} />
        <img src={searchIcon} className="bg-white shadow-md rounded-xl p-2 hover:shadow-lg transition-all" onClick={() => setModalSearch(true)} />
      </div>

      <ModalAdd isOpen={modalAdd} onClose={() => setModalAdd(false)} />
      <ModalSearch isOpen={modalSearch} onClose={() => setModalSearch(false)} parametroUrl="nome" urlSearch="responsaveis" campos={["id", "nome", "ni", "cargo", "area"]} />
      <ModalDeleteEdit isOpen={modalDeleteEdit} onClose={() => setModalDeleteEdit(false)} responsaveis={responsaveisSelecionado} />

      <div className="grid grid-cols-1 md:grid-cols-2 gap-3 w-[1100px]">

        {dados.map((responsavel) => (

          <div key={responsavel.id} className="bg-white shadow-md rounded-xl p-4 flex justify-between items-center hover:shadow-lg transition-all">

            <div>
              <p className="text-sm text-gray-500">ID #{responsavel.id}</p>
              <p className="text-lg font-semibold text-gray-800">{responsavel.nome}</p>
            </div>

            <img src={menuIcon} onClick={() => { setResponsaveisSelecionado(responsaveis); setModalDeleteEdit(true); }} className="cursor-pointer w-[35px] h-auto" />

          </div>

        ))}

      </div>

    </div>
  );
}
