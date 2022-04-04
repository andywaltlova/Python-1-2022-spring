class Package:
    def __init__(self, address, weight):
        self.address = address
        self.weight = weight
        self.delivered = False

    def deliver(self):
        self.delivered = True

    def __str__(self):
        if self.delivered:
            deliveredText = "Package was delivered."
        else:
            deliveredText = "Package was not delivered yet."
        return f"Package is being shipped to {self.address} and weights {self.weight}. {deliveredText}"


class Driver:
    def __init__(self, name, packages):
        self.name = name
        self.packages = packages

    def add_package(self, package):
        if package.delivered:
            print('Unable to assign, package has already been delivered.')
        else:
            self.packages.append(package)

    def packages_left(self):
        return len([pkg for pkg in self.packages if not pkg.delivered])


package_A = Package('Brno', 20)
package_B = Package('Praha', 20)

package_C = Package('Olomouc', 20)
package_C.deliver()

driver = Driver('Karel', [package_A])
driver.add_package(package_B) # priradi se
driver.add_package(package_C) # nelze priradit

print(f'Package(s) left to deliver: {driver.packages_left()}')
