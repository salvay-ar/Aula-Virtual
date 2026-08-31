import './Inicio.css'

function App() {
  
  return (
    <>
    <div className='Contenedor' >
        <div className='Contenido'>
          <h1>Iniciar Sesion</h1>
          <h2>Correo Electrónico</h2>
          <input type="text" placeholder='Email - Usuario' className='input' />
          <h2>Contraseña</h2>
          <input type="password" placeholder='Contraseña' className='input' />
          <div className='botones'>
            <button className='button'>Iniciar Sesion</button>
            <h3>¿No tienes una cuenta? <a href="/Registro">Registrate</a></h3>
          </div>
        </div>
    </div>
    </>
  )
}

export default App
