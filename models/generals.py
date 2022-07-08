import enum

class State(enum.Enum):
    recibido = 'recibido'
    prevalidado_tributaria = 'prevalidado_tributaria'
    prerechazado_tributaria = 'prerechazado_tributaria'
    prevalidado_analitica = 'prevalidado_analitica'
    parcialmente_validado_analitica = 'parcialmente_validado_analitica'
    prerechazado_analitica = 'prerechazado_analitica'
    validado = 'validado'
    parcialmente_validado = 'parcialmente_validado'
    rechazado = 'rechazado'
    finalizado = 'finalizado'
