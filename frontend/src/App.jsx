import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import Layout from './components/Layout'
import Inicio from './pages/Inicio'
import Registro from './pages/Registro'
import UnirseClase from './pages/UnirseClase'
import Pizarron from './pages/materias/Pizarron'
import ListadoPersonas from './pages/materias/ListadoPersonas'
import TableroTareas from './pages/materias/TableroTareas'
import Tarea from './pages/materias/Tarea'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Inicio />} />
        <Route path="/registro" element={<Registro />} />

        <Route element={<Layout />}>
          <Route path="/pizarron" element={<Pizarron />} />
          <Route path="/unirse" element={<UnirseClase />} />
          <Route path="/materia/:id/personas" element={<ListadoPersonas />} />
          <Route path="/materia/:id/tablero" element={<TableroTareas />} />
          <Route path="/materia/:id/tarea/:tareaId" element={<Tarea />} />
        </Route>

        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
