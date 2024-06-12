'use client'

import { useEffect, useState } from 'react'
import {getUsuarios,addUsuario,updateUsuario,deleteUsuario} from '../../api'

export default function Home (){  
  const[usuarios, setUsuarios] = useState([])
  const[novoUsuario, setNovoUsuario] = useState({
    nome:'', email:''
  })

  useEffect (()=>{
    fetchUsuarios()
  },[])

  const fetchUsuarios = async ()=>{
    const data = await getUsuarios();
    console.log(data.nome)
  }

}

