"""
Personas, modelos
"""
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from lib.universal_mixin import UniversalMixin
from perseo.extensions import database


class Persona(database.Model, UniversalMixin):
    """Persona"""

    MODELOS = {
        1: "CONFIANZA",
        2: "SINDICALIZADO",
        3: "JUBILADO",
    }

    # Nombre de la tabla
    __tablename__ = "personas"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Clave foránea
    tabulador_id = Column(Integer, ForeignKey("tabuladores.id"), index=True, nullable=False)
    tabulador = relationship("Tabulador", back_populates="personas")

    # Columnas
    rfc = Column(String(13), nullable=False, unique=True)
    nombres = Column(String(256), nullable=False, index=True)
    apellido_primero = Column(String(256), nullable=False, index=True)
    apellido_segundo = Column(String(256), nullable=False, default="", server_default="")
    curp = Column(String(18), nullable=False, default="", server_default="")
    num_empleado = Column(Integer)
    ingreso_gobierno_fecha = Column(Date)
    ingreso_pj_fecha = Column(Date)
    nacimiento_fecha = Column(Date)
    codigo_postal_fiscal = Column(Integer, default=0)
    seguridad_social = Column(String(24))

    # Columna modelo en Persona
    # 1: Confianza
    # 2: Sindicalizado
    # 3: Jubilado
    modelo = Column(Integer, nullable=False, index=True)  # 1: Confianza, 2: Sindicalizado, 3: Jubilado, 4: Beneficiario

    # Hijos
    cuentas = relationship("Cuenta", back_populates="persona")
    nominas = relationship("Nomina", back_populates="persona")
    percepciones_deducciones = relationship("PercepcionDeduccion", back_populates="persona")
    # puestos_historiales = relationship("PuestoHistorial", back_populates="persona")

    @property
    def nombre_completo(self):
        """Nombre completo"""
        return f"{self.nombres} {self.apellido_primero} {self.apellido_segundo}"

    def __repr__(self):
        """Representación"""
        return f"<Persona {self.rfc}>"
