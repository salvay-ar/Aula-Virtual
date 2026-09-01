import { useState } from 'react'
import './UnirseClase.css'

function UnirseClase() {
  const [codigo, setCodigo] = useState('')

  function manejarEnvio(e) {
    e.preventDefault()
  }

  return (
    <div className="unirse-fondo">
      <div className="unirse-card">
        <h1 className="unirse-titulo">Unirse a Clase</h1>
        <p className="unirse-descripcion">
          Pedile el código a tu profesor e ingresalo para unirte a la clase.
        </p>

        <form className="unirse-formulario" onSubmit={manejarEnvio}>
          <label className="unirse-label">Código de Clase</label>
          <input
            className="unirse-input"
            type="text"
            value={codigo}
            onChange={(e) => setCodigo(e.target.value)}
            placeholder="Ej: ABC123"
          />

          <button className="unirse-boton" type="submit">Unirse</button>
        </form>
      </div>
    </div>
  )
}

export default UnirseClase
