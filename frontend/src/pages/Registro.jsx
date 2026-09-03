import { useState } from 'react'
import { Link } from 'react-router-dom'
import './Registro.css'

function Registro() {
  const [nombre, setNombre] = useState('')
  const [email, setEmail] = useState('')
  const [contraseña, setContraseña] = useState('')
  const [confirmar, setConfirmar] = useState('')

  function manejarEnvio(e) {
    e.preventDefault()
  }

  return (
    <div className="fondo1">
      <div className="contenedor1">
        <h1 className="titulo1">Registro - Aula Virtual</h1>

        <form className="formulario1" onSubmit={manejarEnvio}>
          <label className="label1">Nombre Completo</label>
          <input
            className="input1"
            type="text"
            value={nombre}
            onChange={(e) => setNombre(e.target.value)}
          />

          <label className="label1">Correo Electrónico</label>
          <input
            className="input1"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />

          <label className="label1">Contraseña</label>
          <input
            className="input1"
            type="password"
            value={contraseña}
            onChange={(e) => setContraseña(e.target.value)}
          />

          <label className="label1">Confirmar Contraseña</label>
          <input
            className="input1"
            type="password"
            value={confirmar}
            onChange={(e) => setConfirmar(e.target.value)}
          />

          <button className="boton1" type="submit">Crear Cuenta</button>
        </form>

        <p className="link1">
          ¿Ya tenés cuenta? <Link to="/">Iniciar Sesión</Link>
        </p>
      </div>
    </div>
  )
}

export default Registro
