import React, { useState } from 'react';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom';

export function Cadastro() {
    const [user, setUser] = useState('');
    const [password, setPassword] = useState('');
    const [cargoSelecionado, setCargoSelecionado] = useState('');
    const navigate = useNavigate();

    const handleChange = (event) => {
      const { value } = event.target;
      setCargoSelecionado(value);
    };

    const cadastrar = async () => {
        try {
            await axios.post('http://127.0.0.1:8000/api/signup/', {
                username: user,
                password: password,
                cargo: cargoSelecionado
            });
            alert("Usuário cadastrado com sucesso!");
            navigate('/Home');
        } catch (error) {
            console.error("Erro ao cadastrar usuário:", error);
            alert("Erro ao cadastrar. Tente novamente.");
        }
    };

    return (
        <div className="flex items-center justify-center flex-col w-full h-[100vh]">
            <div className='flex  flex-col items-center justify-center mb-20 p-10 shadow-lg'>

                <h1 className='text-[26px] mt-5'>Cadastro</h1>

                <input className="w-[300px] p-1.5 mt-5 border-2 border-gray-300" value={user} onChange={(e) => setUser(e.target.value)} placeholder='User' />

                <input className="w-[300px] p-1.5 mt-2 border-2 border-gray-300" value={password} onChange={(e) => setPassword(e.target.value)} placeholder='Password' type="password" />

                <div className='flex gap-4 mt-4'>
                    {['Gestor', 'Manutentor', 'Responsavel'].map((cargo) => (
                        <div className='flex gap-1' key={cargo}>
                            <input
                                type="checkbox"
                                id={cargo}
                                name="cargo"
                                value={cargo}
                                checked={cargoSelecionado === cargo}
                                onChange={handleChange}
                            />
                            <label htmlFor={cargo}>{cargo}</label>
                        </div>
                    ))}
                </div>


                <button className="w-[100px] mt-5 p-1 bg-[#007bc0] text-white text-[18px]" onClick={cadastrar}>Cadastrar</button>

                <h4 className="mt-3 text-[20px]">Já possui uma Conta? <Link to="/" className='text-[#007bc0]' >Fazer Login</Link></h4>

            </div>
        </div>
    );
}
