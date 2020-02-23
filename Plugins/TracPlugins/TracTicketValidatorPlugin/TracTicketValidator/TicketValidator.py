#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from trac.config import BoolOption, ListOption
from trac.core import Component, implements
from trac.ticket.api import ITicketManipulator

class TicketsValidator(Component):
    """ Validate ticket fields.

    When we create a ticket, the information in the ticket must be correct
    """

    implements(ITicketManipulator)

    validate_flag = BoolOption('TicketValidator', 'validate_flag', False)
    validates = ListOption('TicketValidator', 'validates', [])

    # ITicketManipulator methods
    def prepare_ticket(self, req, ticket, fields, actions):
        pass

    def validate_ticket(self, req, ticket):
        if self.validate_flag:
            if re.match(r'/newticket/?', req.path_info):
                errorMessage = self._validateSpec(req, ticket)
                if errorMessage:
                    yield None, errorMessage

        for field in self.validates:
            errorMessage = self._validateField(req, ticket, field)
            if errorMessage:
                yield None, errorMessage

    # Private methods
    def _validateSpec(self, req, ticket):
        # Get default attribute
        summary_of_current_ticket = ticket.values.get("summary")
        # reporter = ticket.values.get("reporter")
        # owner = ticket.values.get("owner")
        # priority = ticket.values.get("priority")
        # component = ticket.values.get("component")
        # keywords = ticket.values.get("keywords")
        # version = ticket.values.get("version")
        errorMessage = self.config.get('TicketValidator',
                                       'summary.tip',
                                       "Ticket field is not filled correctly.")
        query = u"SELECT id FROM ticket WHERE summary = '{0}'".format(summary_of_current_ticket)
        result = self.env.db_query(query)
        if len(result) != 0:
            return errorMessage

    def _validateField(self, req, ticket, field):
        # Get error message
        errorMessage = self.config.get('TicketValidator', '%s.tip' % field,
                                       "Ticket field is not filled correctly.")

        # Validate field
        rule = self.config.get('TicketValidator', '%s.rule' % field, None)

        fieldValue = None
        if field in ticket.values:
            fieldValue = ticket.values.get(field)
        elif field in req.args:
            fieldValue = req.args.get(field)

        if fieldValue is not None and \
                rule and re.match(rule, fieldValue) is None:
            return errorMessage
