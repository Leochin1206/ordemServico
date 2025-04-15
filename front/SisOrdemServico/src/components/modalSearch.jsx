import React, { useState } from "react";
import axios from "axios";

export function ModalSearch({ isOpen, onClose, parametroUrl, urlSearch, campos = [] }) {
    if (!isOpen) return null;

    const [formData, setFormData] = useState({ termo: "" });
    const [searchResult, setSearchResult] = useState(null);
    const token = localStorage.getItem('token');

    const handleChange = (e) => {
        setFormData({ ...formData, termo: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {

            console.log(`api/${urlSearch}/search/?${parametroUrl}=${formData.termo}`)
            const response = await axios.get(`http://127.0.0.1:8000/api/${urlSearch}/search/?${parametroUrl}=${formData.termo}`, {
                headers: { Authorization: `Bearer ${token}` },
            });

            const dados = Array.isArray(response.data) ? response.data : [response.data];
            const termoBusca = formData.termo.toLowerCase();

            const filtrados = dados.filter(item =>
                item.nome?.toLowerCase().includes(termoBusca) ||
                item.descricao?.toLowerCase().includes(termoBusca) ||
                item.descricao_servico?.toLowerCase().includes(termoBusca) ||
                item.id?.toString().includes(termoBusca) ||
                item.ni?.toString().includes(termoBusca)
            );

            setSearchResult(filtrados);
            console.log(filtrados);
        } catch (error) {
            console.error("Erro ao buscar:", error);
        }
    };

    return (
        <div className="fixed inset-0 flex items-center justify-center bg-gray-500/30 z-50">
            <div className="bg-white rounded-lg p-6 w-[700px] shadow-lg">
                <h2 className="text-xl font-bold mb-4 text-gray-800">Pesquisar por Nome</h2>

                <form onSubmit={handleSubmit} className="space-y-4">
                    <input
                        type="text"
                        name="termo"
                        placeholder="Digite o Nome"
                        value={formData.termo}
                        onChange={handleChange}
                        className="w-full border border-gray-300 rounded px-3 py-2"
                        required
                    />

                    {searchResult && searchResult.length > 0 && (
                        <div className="bg-gray-100 p-4 rounded space-y-4 max-h-64 overflow-y-auto">
                            {searchResult.map((item, index) => (
                                <div key={index} className="border-b pb-2">
                                    {campos.map((campo) => (
                                        <p key={campo}>
                                            <strong>{campo.charAt(0).toUpperCase() + campo.slice(1)}:</strong>{" "}
                                            {item[campo]}
                                        </p>
                                    ))}
                                </div>
                            ))}
                        </div>
                    )}

                    <div className="flex justify-between mt-4">
                        <button type="submit" className="bg-[#007bc0] text-white px-4 py-2 rounded hover:bg-[#0063c0]">Pesquisar</button>
                        <button type="button" onClick={onClose} className="bg-gray-300 text-gray-800 px-4 py-2 rounded hover:bg-gray-400">Cancelar</button>
                    </div>
                </form>
            </div>
        </div>
    );
}
