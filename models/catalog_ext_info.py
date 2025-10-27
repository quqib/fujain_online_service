from sqlalchemy import Column, String, Integer, Date, LargeBinary, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CatalogExtInfo(Base):
    __tablename__ = 'catalog_ext_info'

    # 主键：虽然原表是 NULL，但建议在 ORM 中设为主键以确保映射唯一性
    rowguid = Column(String(50), primary_key=True, nullable=True, comment='主键')

    # 外键关联 catalog_info.rowguid（逻辑外键）
    catalog_guid = Column(String(50), nullable=True, comment='目录唯一主键')

    anticipate_day = Column(String(50), nullable=True, comment='法定时限')
    promise_day = Column(String(50), nullable=True, comment='承诺时限')
    special_program = Column(String(500), nullable=True, comment='特殊程序')
    limit_explain = Column(LargeBinary, nullable=True, comment='数量限制')  # BLOB -> bytes
    serve_type = Column(String(20), nullable=True, comment='服务对象')
    theme_legal_type = Column(String(40), nullable=True, comment='法人主题')
    theme_natural_type = Column(String(40), nullable=True, comment='个人主题')
    result_type = Column(String(30), nullable=True, comment='审批结果类型')
    result_name = Column(String(200), nullable=True, comment='审批结果名称')
    result_guid = Column(String(500), nullable=True, comment='审批结果样表')
    accept_condition = Column(LargeBinary, nullable=True, comment='受理条件')  # BLOB
    is_fee = Column(String(2), nullable=True, comment='是否收费')
    charge_by_law = Column(String(2000), nullable=True, comment='收费依据')
    is_service = Column(String(2), nullable=True, comment='是否有中介服务')
    service_dept = Column(String(500), nullable=True, comment='中介服务清单')
    othersuggestfields = Column(LargeBinary, nullable=True, comment='其他管控要素')  # BLOB
    othersuggestfieldsvalue = Column(LargeBinary, nullable=True, comment='其他管控要素值')  # BLOB
    flow_chart = Column(String(500), nullable=True, comment='流程图')
    inform_promise_file = Column(String(500), nullable=True, comment='告知承诺书')
    create_date = Column(Date, nullable=True, comment='创建时间')
    state = Column(String(1), nullable=True, comment='状态')
    update_date = Column(Date, nullable=True, comment='更新时间')

    def __repr__(self):
        return f"<CatalogExtInfo(rowguid={self.rowguid}, catalog_guid={self.catalog_guid})>"