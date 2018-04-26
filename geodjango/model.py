# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.contrib.gis.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EduCampoQuadraA(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    tipocampoq = models.CharField(max_length=13, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=13, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edu_campo_quadra_a'


class EduCampoQuadraP(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    tipocampoq = models.CharField(max_length=13, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=13, blank=True, null=True)
    geom = models.PointField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edu_campo_quadra_p'


class EduEdifConstLazerP(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    tipoedifla = models.CharField(max_length=19, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=13, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    geom = models.PointField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edu_edif_const_lazer_p'


class EduEdifConstTuristicaP(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    tipoediftu = models.CharField(max_length=12, blank=True, null=True)
    ovgd = models.CharField(max_length=12, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=13, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    geom = models.PointField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edu_edif_const_turistica_p'


class EduEdifEnsinoP(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    tipoclasse = models.CharField(max_length=100, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    situacaofi = models.CharField(max_length=13, blank=True, null=True)
    geom = models.PointField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edu_edif_ensino_p'


class EduEdifReligiosaP(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    religiao = models.CharField(max_length=100, blank=True, null=True)
    tipoedifre = models.CharField(max_length=12, blank=True, null=True)
    ensino = models.CharField(max_length=12, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=13, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    geom = models.PointField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edu_edif_religiosa_p'


class EduPistaCompeticaoL(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    tipopista = models.CharField(max_length=18, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=13, blank=True, null=True)
    geom = models.MultiLineStringField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edu_pista_competicao_l'


class EduRuinaP(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    geom = models.PointField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edu_ruina_p'


class HidBancoAreiaA(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    tipobanco = models.CharField(max_length=14, blank=True, null=True)
    situacaoem = models.CharField(max_length=17, blank=True, null=True)
    materialpr = models.CharField(max_length=27, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_banco_areia_a'


class HidBarragemA(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    usoprincip = models.CharField(max_length=15, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=13, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_barragem_a'


class HidBarragemL(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    usoprincip = models.CharField(max_length=15, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=13, blank=True, null=True)
    geom = models.MultiLineStringField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_barragem_l'


class HidConfluenciaP(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    geom = models.PointField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_confluencia_p'


class HidCorredeiraA(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_corredeira_a'


class HidCorredeiraL(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    geom = models.MultiLineStringField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_corredeira_l'


class HidCorredeiraP(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    geom = models.PointField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_corredeira_p'


class HidFozMaritimaL(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    geom = models.MultiLineStringField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_foz_maritima_l'


class HidIlhaA(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    tipoilha = models.CharField(max_length=8, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_ilha_a'


class HidLimiteMassaDaguaL(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    alturamedi = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tipolimmas = models.CharField(max_length=51, blank=True, null=True)
    materialpr = models.CharField(max_length=27, blank=True, null=True)
    geom = models.MultiLineStringField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_limite_massa_dagua_l'


class HidMassaDaguaA(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    tipomassad = models.CharField(max_length=18, blank=True, null=True)
    salinidade = models.CharField(max_length=16, blank=True, null=True)
    regime = models.CharField(max_length=31, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_massa_dagua_a'


class HidPontoDrenagemP(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    relacionad = models.CharField(max_length=30, blank=True, null=True)
    geom = models.PointField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_ponto_drenagem_p'


class HidPontoInicioDrenagemP(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    nascente = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_ponto_inicio_drenagem_p'


class HidQuedaDaguaL(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    altura = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tipoqueda = models.CharField(max_length=15, blank=True, null=True)
    geom = models.MultiLineStringField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_queda_dagua_l'


class HidQuedaDaguaP(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    altura = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tipoqueda = models.CharField(max_length=15, blank=True, null=True)
    geom = models.PointField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_queda_dagua_p'


class HidRochaEmAguaA(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    alturalami = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    situacaoem = models.CharField(max_length=17, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_rocha_em_agua_a'


class HidSumidouroVertedouroP(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    causa = models.CharField(max_length=25, blank=True, null=True)
    tiposumver = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_sumidouro_vertedouro_p'


class HidTerrenoSujeitoInundacaoA(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    periodicid = models.CharField(max_length=20, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_terreno_sujeito_inundacao_a'


class HidTrechoDrenagemL(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    dentrodepo = models.CharField(max_length=3, blank=True, null=True)
    compartilh = models.CharField(max_length=3, blank=True, null=True)
    eixoprinci = models.CharField(max_length=3, blank=True, null=True)
    caladomax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    larguramed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    velocidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    profundida = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    coincideco = models.CharField(max_length=35, blank=True, null=True)
    navegabili = models.CharField(max_length=16, blank=True, null=True)
    regime = models.CharField(max_length=31, blank=True, null=True)
    geom = models.MultiLineStringField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_trecho_drenagem_l'


class HidTrechoMassaDaguaA(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    tipotrecho = models.CharField(max_length=13, blank=True, null=True)
    salinidade = models.CharField(max_length=16, blank=True, null=True)
    regime = models.CharField(max_length=31, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_trecho_massa_dagua_a'


class Layer(models.Model):
    topology = models.ForeignKey('Topology', models.DO_NOTHING, primary_key=True)
    layer_id = models.IntegerField()
    schema_name = models.CharField(max_length=-1)
    table_name = models.CharField(max_length=-1)
    feature_column = models.CharField(max_length=-1)
    feature_type = models.IntegerField()
    level = models.IntegerField()
    child_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layer'
        unique_together = (('topology', 'layer_id'), ('schema_name', 'table_name', 'feature_column'),)


class LimMarcoDeLimiteP(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    tipomarcol = models.CharField(max_length=13, blank=True, null=True)
    latitude = models.CharField(max_length=15, blank=True, null=True)
    longitude = models.CharField(max_length=15, blank=True, null=True)
    altitudeor = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    orgresp = models.CharField(max_length=10, blank=True, null=True)
    sistemageo = models.CharField(max_length=16, blank=True, null=True)
    outrarefpl = models.CharField(max_length=20, blank=True, null=True)
    outrarefal = models.CharField(max_length=20, blank=True, null=True)
    geom = models.PointField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_marco_de_limite_p'


class LimMunicipioA(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    geocodigo = models.CharField(max_length=15, blank=True, null=True)
    anoderefer = models.FloatField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_municipio_a'


class LimOutrasUnidProtegidasP(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    anocriacao = models.FloatField(blank=True, null=True)
    sigla = models.CharField(max_length=6, blank=True, null=True)
    areaoficia = models.CharField(max_length=15, blank=True, null=True)
    administra = models.CharField(max_length=18, blank=True, null=True)
    tipooutuni = models.CharField(max_length=30, blank=True, null=True)
    historicom = models.CharField(max_length=254, blank=True, null=True)
    geom = models.PointField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_outras_unid_protegidas_p'


class LimOutrosLimitesOficiaisL(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    coincideco = models.CharField(max_length=50, blank=True, null=True)
    extensao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    obssituaca = models.CharField(max_length=100, blank=True, null=True)
    tipooutlim = models.CharField(max_length=50, blank=True, null=True)
    geom = models.MultiLineStringField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_outros_limites_oficiais_l'


class PtoPtoControleP(models.Model):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nomeabrev = models.CharField(max_length=100, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    latitude = models.CharField(max_length=15, blank=True, null=True)
    longitude = models.CharField(max_length=15, blank=True, null=True)
    altitudeor = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    outrarefpl = models.CharField(max_length=20, blank=True, null=True)
    outrarefal = models.CharField(max_length=20, blank=True, null=True)
    orgaoenter = models.CharField(max_length=30, blank=True, null=True)
    codponto = models.CharField(max_length=9, blank=True, null=True)
    obs = models.CharField(max_length=254, blank=True, null=True)
    codprojeto = models.CharField(max_length=254, blank=True, null=True)
    tiporef = models.CharField(max_length=16, blank=True, null=True)
    sistemageo = models.CharField(max_length=16, blank=True, null=True)
    tipoptocon = models.CharField(max_length=30, blank=True, null=True)
    geom = models.PointField(srid=4674, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pto_pto_controle_p'


class Topology(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    srid = models.IntegerField()
    precision = models.FloatField()
    hasz = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'topology'
