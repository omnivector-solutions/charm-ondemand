# OnDemand

## Build
To build the ondemand charm, clone the project and build the charm using charmcraft.
```bash
git clone https://username@github.com/omnivector-solutions/charm-ondemand
cd charm-ondemand

# make sure dispatch is executable
chmod +x dispatch

# make sure build-charm is executable
chmod +x scripts/build-charm.sh

make build
```
This should produce a charm file, `ondemand.charm`.


## Deploy
Use juju to deploy the charm and relate it to the desired infrastructure in the model.
```bash
juju deploy ./ondemand.charm
```