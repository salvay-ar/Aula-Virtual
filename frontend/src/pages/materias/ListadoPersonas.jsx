import { Link, useParams } from 'react-router-dom'
import './ListadoPersonas.css'

const materias = [
  { id: 1, nombre: 'Matemáticas' },
  { id: 2, nombre: 'Lengua y Literatura' },
  { id: 3, nombre: 'Historia' },
  { id: 4, nombre: 'Ciencias Naturales' },
]

const personas = [
  { id: 1, nombre: 'Profesor Ejemplo', rol: 'Profesor' },
  { id: 2, nombre: 'Alumno Uno', rol: 'Alumno' },
  { id: 3, nombre: 'Alumno Dos', rol: 'Alumno' },
  { id: 4, nombre: 'Alumno Tres', rol: 'Alumno' },
]

function ListadoPersonas() {
  const { id } = useParams()
  const materia = materias.find((m) => m.id === Number(id))

  return (
    <div className="personas">
      <header className="personas-header">
        <h1 className="personas-titulo">Listado de Personas</h1>
        <p className="personas-subtitulo">
          {materia ? materia.nombre : 'Personas de la materia'}
        </p>

        <div className="personas-links">
          <Link to={`/materia/${id}/tablero`} className="personas-link-tablero">
            Ver tablero de tareas
          </Link>
        </div>
      </header>

      <ul className="personas-lista">
        {personas.map((persona) => (
          <li key={persona.id} className="persona-item">
            <div className="persona-avatar">
              {persona.nombre.charAt(0)}
            </div>
            <div className="persona-info">
              <span className="persona-nombre">{persona.nombre}</span>
              <span className="persona-rol">{persona.rol}</span>
            </div>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default ListadoPersonas
