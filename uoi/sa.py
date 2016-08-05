# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy import create_engine, DateTime, Text, and_, insert, or_
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def initdb(credentials, debug):
    engine = create_engine(credentials, convert_unicode=True, echo=debug)
    Base.metadata.create_all(bind=engine)

def connect(credentials, debug):
    engine = create_engine(credentials, echo=debug)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

Base = declarative_base()
metadata = Base.metadata

class Asset(Base):
    __tablename__ = 'Assets'

    id = Column(Integer, primary_key=True)
    hypervisor_id = Column(ForeignKey(u'Hypervisors.id'), index=True)
    processor_id = Column(ForeignKey(u'Processors.id'), unique=True)
    region_id = Column(ForeignKey(u'Regions.id'), index=True)
    role_id = Column(ForeignKey(u'Roles.id'), index=True)
    ipmi_id = Column(ForeignKey(u'Ipmi.id'), unique=True)
    configuration_id = Column(ForeignKey(u'Configurations.id'), unique=True)
    environment_id = Column(ForeignKey(u'Environments.id'), index=True)
    created = Column(DateTime, nullable=False)
    mac = Column(String(17, u'utf8_unicode_ci'), nullable=False, unique=True)
    uuid = Column(String(255, u'utf8_unicode_ci'), nullable=False)
    vendor = Column(String(255, u'utf8_unicode_ci'), nullable=False)
    type = Column(String(255, u'utf8_unicode_ci'), nullable=False)
    status = Column(Integer, nullable=False)

    configuration = relationship(u'Configuration')
    environment = relationship(u'Environment')
    hypervisor = relationship(u'Hypervisor')
    ipmi = relationship(u'Ipmi')
    processor = relationship(u'Processor')
    region = relationship(u'Region')
    role = relationship(u'Role')


class Common(Base):
    __tablename__ = 'Commons'

    id = Column(Integer, primary_key=True)
    name = Column(String(255, u'utf8_unicode_ci'), nullable=False)
    description = Column(Text(collation=u'utf8_unicode_ci'), nullable=False)
    ntp = Column(Text(collation=u'utf8_unicode_ci'), nullable=False)
    dns = Column(Text(collation=u'utf8_unicode_ci'), nullable=False)
    domain = Column(String(255, u'utf8_unicode_ci'), nullable=False)
    selinux = Column(String(255, u'utf8_unicode_ci'), nullable=False)
    sshkey = Column(Text(collation=u'utf8_unicode_ci'), nullable=False)
    rootpwd = Column(String(255, u'utf8_unicode_ci'), nullable=False)
    packages = Column(Text(collation=u'utf8_unicode_ci'), nullable=False)
    status = Column(Integer, nullable=False)


class Configuration(Base):
    __tablename__ = 'Configurations'

    id = Column(Integer, primary_key=True)
    hostname = Column(String(255, u'utf8_unicode_ci'), nullable=False, unique=True)
    domain = Column(String(255, u'utf8_unicode_ci'), nullable=False)
    distribution = Column(String(255, u'utf8_unicode_ci'), nullable=False)
    extraconf = Column(Text(collation=u'utf8_unicode_ci'), nullable=False)


class Environment(Base):
    __tablename__ = 'Environments'

    id = Column(Integer, primary_key=True)
    common_id = Column(ForeignKey(u'Commons.id'), unique=True)
    name = Column(String(255, u'utf8_unicode_ci'), nullable=False)
    description = Column(Text(collation=u'utf8_unicode_ci'), nullable=False)
    status = Column(Integer, nullable=False)

    common = relationship(u'Common')


class Hypervisor(Base):
    __tablename__ = 'Hypervisors'

    id = Column(Integer, primary_key=True)
    name = Column(String(255, u'utf8_unicode_ci'), nullable=False, unique=True)
    address = Column(String(15, u'utf8_unicode_ci'), nullable=False, unique=True)
    description = Column(Text(collation=u'utf8_unicode_ci'), nullable=False)
    status = Column(Integer, nullable=False)


class Ipmi(Base):
    __tablename__ = 'Ipmi'

    id = Column(Integer, primary_key=True)
    address = Column(String(15, u'utf8_unicode_ci'), nullable=False, unique=True)
    user = Column(String(255, u'utf8_unicode_ci'), nullable=False)
    password = Column(String(255, u'utf8_unicode_ci'), nullable=False)


class Network(Base):
    __tablename__ = 'Networks'

    id = Column(Integer, primary_key=True)
    asset_id = Column(ForeignKey(u'Assets.id'), index=True)
    type = Column(String(255, u'utf8_unicode_ci'), nullable=False)
    interface = Column(String(255, u'utf8_unicode_ci'), nullable=False)
    ipaddr = Column(String(15, u'utf8_unicode_ci'), nullable=False)
    netmask = Column(String(15, u'utf8_unicode_ci'), nullable=False)
    gateway = Column(String(15, u'utf8_unicode_ci'), nullable=False)
    slaveof = Column(String(255, u'utf8_unicode_ci'), nullable=False)
    master = Column(Boolean, nullable=False)
    mtu = Column(Integer, nullable=False)
    options = Column(Text(collation=u'utf8_unicode_ci'))
    vlanid = Column(String(4, u'utf8_unicode_ci'))
    status = Column(Boolean, nullable=False)

    asset = relationship(u'Asset')


class Nic(Base):
    __tablename__ = 'Nics'

    id = Column(Integer, primary_key=True)
    asset_id = Column(ForeignKey(u'Assets.id'), index=True)
    device = Column(String(255, u'utf8_unicode_ci'), nullable=False)
    mac = Column(String(255, u'utf8_unicode_ci'), nullable=False)
    state = Column(String(255, u'utf8_unicode_ci'), nullable=False)
    speed = Column(Integer, nullable=False)
    vendor = Column(String(255, u'utf8_unicode_ci'), nullable=False)

    asset = relationship(u'Asset')


class Processor(Base):
    __tablename__ = 'Processors'

    id = Column(Integer, primary_key=True)
    core = Column(Integer, nullable=False)
    physical = Column(Integer, nullable=False)
    model = Column(String(255, u'utf8_unicode_ci'), nullable=False)
    freq = Column(String(255, u'utf8_unicode_ci'), nullable=False)


class Region(Base):
    __tablename__ = 'Regions'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    name = Column(String(255, u'utf8_unicode_ci'), nullable=False, unique=True)


class Role(Base):
    __tablename__ = 'Roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(255, u'utf8_unicode_ci'), nullable=False, unique=True)
    created = Column(DateTime, nullable=False)
    description = Column(Text(collation=u'utf8_unicode_ci'), nullable=False)
    status = Column(Integer, nullable=False)

t_asset = Asset()
t_common = Common()
t_configuration = Configuration()
t_environment = Environment()
t_hypervisor = Hypervisor()
t_ipmi = Ipmi()
t_network = Network()
t_nic = Nic()
t_processor = Processor()
t_region = Region()
t_role = Role()
