# OnDemand

## Build
To build the ondemand charm, clone the project and build the charm using charmcraft.
```bash
git clone https://username@github.com/omnivector-solutions/charm-ondemand

# make sure dispatch is executable
chmod +x /charm-ondemand/dispatch

charmcraft build --from ./charm-ondemand
```
This should produce a charm file, `ondemand.charm`.


## Deploy
Use juju to deploy the charm and relate it to the desired infrastructure in the model.
```bash
juju deploy ./ondemand.charm
```