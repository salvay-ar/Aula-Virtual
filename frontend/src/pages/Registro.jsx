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
    <div className="registro-fondo">
      <div className="registro-card">
        <h1 className="registro-titulo">Registro</h1>

        <form className="registro-formulario" onSubmit={manejarEnvio}>
          <label className="registro-label">Nombre Completo</label>
          <input
            className="registro-input"
            type="text"
            value={nombre}
            onChange={(e) => setNombre(e.target.value)}
          />

          <label className="registro-label">Correo Electrónico</label>
          <input
            className="registro-input"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />

          <label className="registro-label">Contraseña</label>
          <input
            className="registro-input"
            type="password"
            value={contraseña}
            onChange={(e) => setContraseña(e.target.value)}
          />

          <label className="registro-label">Confirmar Contraseña</label>
          <input
            className="registro-input"
            type="password"
            value={confirmar}
            onChange={(e) => setConfirmar(e.target.value)}
          />

          <button className="registro-boton" type="submit">Crear Cuenta</button>
        </form>

        <p className="registro-link">
          ¿Ya tenés cuenta? <Link to="/">Iniciar Sesión</Link>
        </p>
      </div>
    </div>
  )
}

export default Registro
