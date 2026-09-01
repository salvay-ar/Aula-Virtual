import { Link } from 'react-router-dom'
import './Pizarron.css'

const materias = [
  { id: 1, nombre: 'Matemáticas', descripcion: 'Álgebra y cálculo' },
  { id: 2, nombre: 'Lengua y Literatura', descripcion: 'Gramática y lectura' },
  { id: 3, nombre: 'Historia', descripcion: 'Historia universal' },
  { id: 4, nombre: 'Ciencias Naturales', descripcion: 'Biología y química' },
]

function Pizarron() {
  return (
    <div className="pizarron">
      <header className="pizarron-header">
        <h1 className="pizarron-titulo">Mis Clases</h1>
        <p className="pizarron-subtitulo">Todas las clases</p>
      </header>

      <main className="pizarron-grid">
        {materias.map((materia) => (
          <Link
            key={materia.id}
            to={`/materia/${materia.id}/tablero`}
            className="pizarron-card"
          >
            <h2 className="pizarron-card-nombre">{materia.nombre}</h2>
            <p className="pizarron-card-descripcion">{materia.descripcion}</p>
          </Link>
        ))}
      </main>
    </div>
  )
}

export default Pizarron
