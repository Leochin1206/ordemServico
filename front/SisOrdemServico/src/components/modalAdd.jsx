import React, { useState, useEffect } from "react";
import axios from "axios";

export function ModalAdd({ isOpen, onClose, titulo, url, campos = [] }) {
    if (!isOpen) return null;

    // Inicializar o estado com os campos fornecidos
    const [formData, setFormData] = useState({});

    useEffect(() => {
        // Quando os campos mudarem, inicializar o estado com campos vazios
        const initialFormData = campos.reduce((acc, campo) => {
            acc[campo] = ''; // Define o valor inicial como vazio
            return acc;
        }, {});
        setFormData(initialFormData);
    }, [campos]);

    const token = localStorage.getItem('token');

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!token) {
            alert("Token não encontrado. Faça login novamente.");
            return;
        }

        try {
            const response = await axios.post(`http://127.0.0.1:8000/api/${url}`, formData, {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });

            alert("Cadastro realizado com sucesso!");
            onClose();
        } catch (error) {
            console.error("Erro ao cadastrar:", error);
            alert("Erro ao cadastrar.");
        }
    };

    return (
        <div className="fixed inset-0 flex items-center justify-center bg-gray-500/30 z-50">
            <div className="bg-white rounded-lg p-6 w-[700px] shadow-lg">
                <h2 className="text-xl font-bold mb-4 text-gray-800">Adicionar novo {titulo}</h2>

                <form onSubmit={handleSubmit}>
                    {campos.map((campo) => (
                        <div key={campo} className="mb-4">
                            <label htmlFor={campo} className="block text-gray-700">{campo}</label>
                            <input
                                type="text"
                                id={campo}
                                name={campo}
                                placeholder={campo}
                                value={formData[campo] || ''}
                                onChange={handleChange}
                                className="w-full p-2 border border-gray-300 rounded-md"
                                required
                            />
                        </div>
                    ))}

                    <div className="flex justify-end gap-4">
                        <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded-md">Salvar</button>
                        <button type="button" onClick={onClose} className="bg-gray-300 text-gray-700 px-4 py-2 rounded-md">Cancelar</button>
                    </div>
                </form>
            </div>
        </div>
    );
}
