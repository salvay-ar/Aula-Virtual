import { NavLink, Outlet } from 'react-router-dom'
import './Layout.css'

function Layout() {
  return (
    <div className="layout">
      <nav className="layout-nav">
        <span className="layout-logo">Aula Virtual</span>
        <div className="layout-links">
          <NavLink
            to="/pizarron"
            className={({ isActive }) =>
              isActive ? 'layout-link active' : 'layout-link'
            }
          >
            Mis Cursos
          </NavLink>
          <NavLink
            to="/unirse"
            className={({ isActive }) =>
              isActive ? 'layout-link active' : 'layout-link'
            }
          >
            Nuevo Curso
          </NavLink>
        </div>
        <NavLink to="/" className="layout-cerrar">
          Cerrar Sesión
        </NavLink>
      </nav>

      <main className="layout-contenido">
        <Outlet />
      </main>
    </div>
  )
}

export default Layout
