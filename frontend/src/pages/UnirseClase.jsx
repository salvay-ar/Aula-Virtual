import { useState } from 'react'
import './UnirseClase.css'

function UnirseClase() {
  const [codigo, setCodigo] = useState('')

  function manejarEnvio(e) {
    e.preventDefault()
  }

  return (
    <div className="fondoUnirse">
      <div className="contenedorUnirse">
        <h1 className="tituloUnirse">Unirse a Clase</h1>
        <p className="descripcionUnirse">
          Pedile el código a tu profesor e ingresalo para unirte a la clase.
        </p>

        <form className="formularioUnirse" onSubmit={manejarEnvio}>
          <label className="labelUnirse">Código de Clase</label>
          <input
            className="inputUnirse"
            type="text"
            value={codigo}
            onChange={(e) => setCodigo(e.target.value)}
            placeholder="Ej: ABC123"
          />

          <button className="botonUnirse" type="submit">Unirse</button>
        </form>
      </div>
    </div>
  )
}

export default UnirseClase
