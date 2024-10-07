class JavaInfo:
  def __init__(self):
    self.name = "Java"
    self.author = "James Gosling"

java = JavaInfo()

# getattr
print(f"{'-'*35} getattr {'-'*35}")
print(getattr(java, "name"))
print(getattr(java, "not defined", "default value"))

# setattr
print(f"{'-'*35} setattr {'-'*35}")
print(getattr(java, "invented", None))
setattr(java, "invented", 1995)
print(getattr(java, "invented", None))

# hasattr
print(f"{'-'*35} hasattr {'-'*35}")
print(hasattr(java, "author"))
print(hasattr(JavaInfo, "my_name")) # Its also used to check a class has any class variables

# delattr
print(f"{'-'*35} delattr {'-'*35}")
print(hasattr(java, "name"))
delattr(java, "name")
print(hasattr(java, "name"))