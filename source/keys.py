def enum(**enums):
    return type('Enum', (), enums)

Keys = enum(yoVoy='$yovoy',help='$help',yaNoVoy='$yanovoy',cleanAll='$cleanall')
