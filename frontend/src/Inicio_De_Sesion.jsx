import './Inicio.css'

function App() {

  return (
    <>
    <div className='Fondo' >
      <img className='Logo'></img>
      <div className='float'>
        <h1 className='titulo'> Iniciar Sesion </h1>
          <h1 className='Texto'> Correo Electronico </h1>
        <input className='Correo' type='text'/>
          <h1 className='Texto'> Contraseña </h1>
        <input className='Contraseña' type="text"/>
            <div className='Completado'>
                <h1 className='ya tenes' > ¿No tienes cuenta? </h1>
                <h1 className='Ruteo' > Registrarse </h1>
            </div>
      </div>
    </div>
    </>
  )
}

export default App
