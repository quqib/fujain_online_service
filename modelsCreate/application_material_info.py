"""
申报材料表
"""
from sqlalchemy import Column, String, Text, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ApplicationMaterialInfo(Base):
    __tablename__ = 'application_material_info'

    # 主键
    rowguid = Column(String(50), primary_key=True, nullable=False, comment='主键')

    # 文件类型
    file_type = Column(String(100), nullable=True, comment='文件类型')
    # 示例：身份证、营业执照、申请表、承诺书、合同等

    # 材料形式（纸质/电子/原件/复印件）
    material_form = Column(String(50), nullable=True, comment='材料形式')
    # 建议值：'纸质原件', '纸质复印件', '电子版', '电子证照', '版式文件（OFD/PDF）'

    # 材料要求（概括性描述）
    material_requirements = Column(String(500), nullable=True, comment='材料要求')
    # 示例：需加盖公章、需法人签字、需年检章等

    # 材料必要性
    material_necessity = Column(String(50), nullable=True, comment='材料必要性')
    # 建议值：'必要', '容缺受理', '非必要', '前置条件'

    # 来源渠道
    source_channel = Column(String(100), nullable=True, comment='来源渠道')
    # 建议值：'申请人自备', '政府部门核发', '第三方机构出具', '系统自动生成'

    # 具体要求（详细说明）
    specific_requirements = Column(Text, nullable=True, comment='具体要求')
    # 可包含格式、内容、签章、有效期等详细说明

    # 设立依据
    basis_of_establishment = Column(Text, nullable=True, comment='设立依据')
    # 法律、法规、规章或政策依据，支持多条文引用

    # 材料核查标准
    material_check_standard = Column(Text, nullable=True, comment='材料核查标准')
    # 审核人员使用的检查清单或判断标准
    # 示例：身份证是否在有效期内、营业执照经营范围是否包含XX

    # 附件下载（存储文件二进制或路径）
    attachment_download = Column(Text, nullable=True, comment='附件下载')
    # 方案1：存储文件路径（推荐）如 "/uploads/templates/申请表.docx"
    # 方案2：若必须存二进制，应使用 LargeBinary，但不推荐大文件直接入库存

    # 首次申请（是否首次申请需要）
    first_application = Column(String(2), nullable=True, comment='首次申请')
    # '1'=是，'0'=否

    # 变更（是否变更申请需要）
    change_application = Column(String(2), nullable=True, comment='变更')
    # '1'=是，'0'=否

    # 审计字段
    create_date = Column(Date, nullable=True, comment='创建日期')
    # update_date = Column(Date, nullable=True, comment='更新时间')
    # state = Column(String(1), nullable=True, comment='状态')  # '1'=有效，'0'=无效

    def __repr__(self):
        return f"<ApplicationMaterialInfo(file_type='{self.file_type}', material_necessity='{self.material_necessity}')>"