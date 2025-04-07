import React from 'react'
import { Routes, Route } from 'react-router-dom'
import './App.css'

import { Ambientes } from './pages/ambientes'
import { Cadastro } from './pages/cadastro'
import { Gestores } from './pages/gestores'
import { Historico } from './pages/historico'
import { Home } from './pages/home'
import { Login } from './pages/login'
import { Manutentores } from './pages/manutentores'
import { OrdemServico } from './pages/ordemServico'
import { Patrimonios } from './pages/patrimonios'
import { Responsaveis } from './pages/responsaveis'


function App() {
  return (
    <Routes>
      <Route path='/' element={<Login />} />
      <Route path='/Cadastro' element={<Cadastro />} />
      <Route path='/Ambientes' element={<Ambientes/>} />
      <Route path='/Gestores' element={<Gestores />} />
      <Route path='/Historico' element={<Historico />} />
      <Route path='/Home' element={<Home />} />
      <Route path='/Manutentores' element={<Manutentores />} />
      <Route path='/OrdemServico' element={<OrdemServico />} />
      <Route path='/Patrimonios' element={<Patrimonios />} />
      <Route path='/Responsaveis' element={<Responsaveis />} />
    </Routes>
  )
}

export default App
