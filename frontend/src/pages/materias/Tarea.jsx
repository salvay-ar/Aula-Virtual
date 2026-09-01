import './Tarea.css'

function Tarea() {
  return (
    <div className="tarea">
      <header className="tarea-header">
        <span className="tarea-tag">Tarea</span>
        <h1 className="tarea-titulo">Título de la Tarea</h1>
        <p className="tarea-fecha">Fecha de entrega: 2026-09-05</p>
      </header>

      <section className="tarea-cuerpo">
        <h2 className="tarea-subtitulo">Descripción</h2>
        <p className="tarea-descripcion">
          Acá va el enunciado de la tarea. Podés describir qué es lo que hay que
          hacer, adjuntar consignas y dejar los materiales necesarios.
        </p>

        <h2 className="tarea-subtitulo">Materiales adjuntos</h2>
        <ul className="tarea-materiales">
          <li className="tarea-material">archivo1.pdf</li>
          <li className="tarea-material">consigna.docx</li>
        </ul>

        <h2 className="tarea-subtitulo">Entrega</h2>
        <button className="tarea-boton" type="button">Subir Entrega</button>
      </section>
    </div>
  )
}

export default Tarea
