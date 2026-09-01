import { Link, useParams } from 'react-router-dom'
import './TableroTareas.css'

const materias = [
  { id: 1, nombre: 'Matemáticas' },
  { id: 2, nombre: 'Lengua y Literatura' },
  { id: 3, nombre: 'Historia' },
  { id: 4, nombre: 'Ciencias Naturales' },
]

const tareas = [
  { id: 1, tipo: 'tarea', titulo: 'Ejercicios del capítulo 3', fecha: '2026-09-05' },
  { id: 2, tipo: 'material', titulo: 'Apuntes de la clase', fecha: '2026-08-28' },
  { id: 3, tipo: 'tarea', titulo: 'Trabajo práctico final', fecha: '2026-09-12' },
  { id: 4, tipo: 'material', titulo: 'Bibliografía recomendada', fecha: '2026-08-20' },
]

function TableroTareas() {
  const { id } = useParams()
  const materia = materias.find((m) => m.id === Number(id))

  return (
    <div className="tablero">
      <header className="tablero-header">
        <h1 className="tablero-titulo">Tablero de Tareas y Materiales</h1>
        <p className="tablero-subtitulo">
          {materia ? materia.nombre : 'Materia'}
        </p>

        <div className="tablero-links">
          <Link
            to={`/materia/${id}/personas`}
            className="tablero-link-personas"
          >
            Personas de la materia
          </Link>
        </div>
      </header>

      <ul className="tablero-lista">
        {tareas.map((item) => {
          const contenido = (
            <>
              <span className={`tablero-tipo ${item.tipo}`}>
                {item.tipo === 'tarea' ? 'Tarea' : 'Material'}
              </span>
              <div className="tablero-info">
                <h3 className="tablero-titulo-item">{item.titulo}</h3>
                <span className="tablero-fecha">{item.fecha}</span>
              </div>
            </>
          )

          return item.tipo === 'tarea' ? (
            <Link
              key={item.id}
              to={`/materia/${id}/tarea/${item.id}`}
              className="tablero-item"
            >
              {contenido}
            </Link>
          ) : (
            <li key={item.id} className="tablero-item tablero-item-material">
              {contenido}
            </li>
          )
        })}
      </ul>
    </div>
  )
}

export default TableroTareas
