from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cars(models.Model):
    car_id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=100)
    year = models.IntegerField(blank=True, null=True)
    license_plate = models.CharField(max_length=20)
    cargo_capacity = models.CharField(max_length=12)
    vin_code = models.CharField(max_length=17)
    cargo_compartment_volume = models.CharField(max_length=20, blank=True, null=True)
    driver = models.ForeignKey('Drivers', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cars'


class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=320)
    phone_number = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'customers'


class DestinationDrivers(models.Model):
    destination_driver_id = models.AutoField(primary_key=True)
    destination = models.ForeignKey('Destinations', models.DO_NOTHING, blank=True, null=True)
    driver = models.ForeignKey('Drivers', models.DO_NOTHING, blank=True, null=True)
    status_shipping = models.TextField()
    date_destination = models.DateField()

    class Meta:
        managed = False
        db_table = 'destination_drivers'


class Destinations(models.Model):
    destination_id = models.AutoField(primary_key=True)
    destination_name = models.CharField(max_length=100)
    destination_address = models.CharField(max_length=100)
    cargo_type = models.CharField(max_length=50, blank=True, null=True)
    driver = models.ForeignKey('Drivers', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'destinations'


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
    id = models.BigAutoField(primary_key=True)
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


class Drivers(models.Model):
    driver_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    driver_license_number = models.CharField(max_length=20)
    driver_license_category = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drivers'


class Invoices(models.Model):
    invoice_id = models.BigAutoField(primary_key=True)
    shipment = models.ForeignKey('Shipments', models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'invoices'


class Payments(models.Model):
    payment_id = models.BigAutoField(primary_key=True)
    shipment = models.ForeignKey('Shipments', models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'payments'


class ProductSpecifications(models.Model):
    specification_id = models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    other_details = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_specifications'


class Roles(models.Model):
    role_id = models.BigAutoField(primary_key=True)
    role_name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'roles'


class Shipments(models.Model):
    shipment_id = models.AutoField(primary_key=True)
    car = models.ForeignKey(Cars, models.DO_NOTHING, blank=True, null=True)
    driver = models.ForeignKey(Drivers, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    destination = models.ForeignKey(Destinations, models.DO_NOTHING, blank=True, null=True)
    departure_date = models.DateTimeField(blank=True, null=True)
    arrival_date = models.DateTimeField(blank=True, null=True)
    quantity_shipped = models.DecimalField(max_digits=65535, decimal_places=65535)
    shipping_cost = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'shipments'


class UserRoles(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, role_id) found, that is not supported. The first column is selected.
    role = models.ForeignKey(Roles, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_roles'
        unique_together = (('user', 'role'),)


class Users(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=255)
    password_hash = models.CharField(max_length=255, validators=[RegexValidator(
        r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[A-Za-z\d!@#$%^&*(),.?":{}|<>]{8,}$',
        message='Password must contain at least one uppercase letter, one lowercase letter, one digit, one special character, and be at least 8 characters long.'
    )])
    email = models.CharField(unique=True, max_length=255)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'users'


class Quote(models.Model):
    departure = models.CharField(max_length=100)
    delivery = models.CharField(max_length=100)
    weight = models.CharField(max_length=12)
    dimensions = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=320)
    phone = models.CharField(max_length=20)
    message = models.TextField()

    