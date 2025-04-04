import React, { useState, useEffect } from "react";
import axios from "axios";

export function Ambientes() {

    const [dados, setDados] = useState([]);
    const token = localStorage.getItem('token');

    console.log(localStorage.getItem("token"));


    useEffect(() => {
        if (!token) return;

        const fetchData = async () => {
            try {
                const response = await axios.get("http://127.0.0.1:8000/api/ambientes", {
                    headers: { Authorization: `Bearer ${token}` },
                });
                setDados(response.data);
                console.log(response.data)
            } catch (error) {
                console.error("Erro ao buscar dados:", error);
            }
        };
        fetchData();
    }, [token]);

    return (
        <div>
            {dados.map((ambientes) => (
                <div key={ambientes.id} className="">
                    <h2>{ambientes.id}</h2>
                    <h2>{ambientes.num_sala}</h2>
                </div>
            ))}
        </div>
    );
}