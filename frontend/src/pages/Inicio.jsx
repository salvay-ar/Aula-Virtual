import { useState } from 'react'
import { Link } from 'react-router-dom'
import './Inicio.css'

function Inicio() {
  const [email, setEmail] = useState('')
  const [contraseña, setContraseña] = useState('')

  function manejarEnvio(e) {
    e.preventDefault()
  }

  return (
    <div className="inicio-fondo">
      <div className="inicio-card">
        <h1 className="inicio-titulo">Iniciar Sesión</h1>

        <form className="inicio-formulario" onSubmit={manejarEnvio}>
          <label className="inicio-label">Correo Electrónico</label>
          <input
            className="inicio-input"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />

          <label className="inicio-label">Contraseña</label>
          <input
            className="inicio-input"
            type="password"
            value={contraseña}
            onChange={(e) => setContraseña(e.target.value)}
          />

          <button className="inicio-boton" type="submit">Iniciar Sesión</button>
        </form>

        <p className="inicio-link">
          ¿No tenés cuenta? <Link to="/registro">Registrate</Link>
        </p>
      </div>
    </div>
  )
}

export default Inicio
