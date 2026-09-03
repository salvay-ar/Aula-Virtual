import { useState } from 'react'
import { Link } from 'react-router-dom'
import './inicioSesion.css'

function Inicio() {
  const [email, setEmail] = useState('')
  const [contraseña, setContraseña] = useState('')

  function manejarEnvio(e) {
    e.preventDefault()
  }

  return (
    <div className="fondo">
      <div className="contenedor">
        <h1 className="tituloh1">Aula Virtual</h1>

        <form className="formulario" onSubmit={manejarEnvio}>
          <label className="label">Correo Electrónico</label>
          <input
            className="input"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />

          <label className="label">Contraseña</label>
          <input
            className="input"
            type="password"
            value={contraseña}
            onChange={(e) => setContraseña(e.target.value)}
          />

          <button className="boton" type="submit">Iniciar Sesión</button>
        </form>

        <p className="link">
          ¿No tenés cuenta? <Link to="/registro">Registrate</Link>
        </p>
      </div>
    </div>
  )
}

export default Inicio
