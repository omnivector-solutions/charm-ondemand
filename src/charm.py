#!/usr/bin/env python3
# Copyright 2021 Matheus Tosta
# See LICENSE file for licensing details.

import logging

from ops.charm import CharmBase
from ops.main import main
from ops.framework import StoredState

from ondemand_ops import OnDemandOps
from version import VERSION

logger = logging.getLogger(__name__)


class OndemandCharm(CharmBase):
    _stored = StoredState()

    def __init__(self, *args):
        super().__init__(*args)

        self._ondemand_ops = OnDemandOps()

        self._stored.set_default(things=[])

        events = {
            self.on.install: self._on_install
        }

        for event, handler in events.items():
            self.framework.observe(event, handler)

    def _on_install(self):

        self.unit.set_workload_version(VERSION)

        # self._ondemand_ops.setup_docker()
        self._ondemand_ops.setup_ondemand()

    def _on_config_changed(self, _):
        current = self.config["thing"]
        if current not in self._stored.things:
            logger.debug("found a new thing: %r", current)
            self._stored.things.append(current)

    def _on_fortune_action(self, event):
        fail = event.params["fail"]
        if fail:
            event.fail(fail)
        else:
            event.set_results({"fortune": "A bug in the code is worth two in the documentation."})


if __name__ == "__main__":
    main(OndemandCharm)
