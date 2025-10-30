"""
权责清单信息表
"""
import uuid
from sqlalchemy import Column, String, CHAR, Text, DateTime, func, ForeignKey
from ..base import Base


class ServiceBasicDutyInfo(Base):
    __tablename__ = 'service_basic_duty_info'

    # 主键：使用 CHAR(36) 存储 UUID 字符串
    rowguid = Column(
        CHAR(36),  # 在数据库中存储为 CHAR(36)
        primary_key=True,
        default=lambda: str(uuid.uuid4()),  # 自动生成 UUID 字符串
        nullable=False,
        comment='主键，UUID 自动生成'
    )

    # 外键：关联到 service_basic_information_info 表的 rowguid
    basic_info_rowguid = Column(
        CHAR(36),
        ForeignKey('service_basic_information_info.rowguid', ondelete='CASCADE'),
        nullable=False,
        comment='关联 service_basic_information_info 表的主键'
    )
    # 类别（如“行政许可”、“行政处罚”、“行政强制”等）
    category = Column(String(100), nullable=True, comment='类别')

    # 权责编码（权责事项唯一编码）
    responsibility_code = Column(String(64), nullable=True, index=True, comment='权责编码')

    # 关联服务事项名称（对应政务服务事项名称）
    associated_service_item_name = Column(String(200), nullable=True, comment='关联服务事项名称')

    # 行使主体（实施该权力的部门名称）
    exercising_body = Column(String(255), nullable=True, comment='行使主体')

    # 行使层级（如“国家级”、“省级”、“市级”、“县级”、“乡级”）
    exercise_level = Column(String(50), nullable=True, comment='行使层级')

    # 实施依据（法律、法规、规章等条文依据，可能多条）
    implementation_basis = Column(Text, nullable=True, comment='实施依据')

    # 备注
    remarks = Column(Text, nullable=True, comment='备注')

    # 创建时间
    create_date = Column(DateTime, nullable=True, default=func.current_timestamp(), comment='创建时间')

    def __repr__(self):
        return f"<ResponsibilityListInfo(responsibility_code='{self.responsibility_code}', category='{self.category}')>"