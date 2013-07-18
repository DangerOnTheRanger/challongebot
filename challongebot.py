import challonge


CHALLONGE_USERNAME = ''
TOURNAMENT_NAME = ''
API_KEY = ''

assert CHALLONGE_USERNAME and TOURNAMENT_NAME and API_KEY != ''
challonge.set_credentials(CHALLONGE_USERNAME, API_KEY)

tournament_id = None
participants = {}
gfwl_ids = {}


def command_setup(willie, trigger):

   if trigger.owner is False:
      willie.say('You can\'t tell me what to do!')
      return

   willie.say('Getting tournament ID...')

   global tournament_id
   tournament_id = challonge.tournaments.show(TOURNAMENT_NAME)['id']

   willie.say('Getting participant list...')
   global participants
   players = challonge.participants.index(tournament_id)
   for player_data in players:
      participants[player_data['id']] = player_data['challonge-username'] or player_data['name']

   willie.say('Finished.')


command_setup.commands = ['setup']
command_setup.priority = 'medium'


def command_pending(willie, trigger):

   willie.say('Pending matches:')
   pending_matches = challonge.matches.index(tournament_id, state='open')

   for match in pending_matches:
      player_1 = participants[match['player1-id']]
      player_1_gfwl = gfwl_id[player_1]
      player_2 = participants[match['player2-id']]
      player_2_gfwl = gfwl_id[player_2]
      willie.say('%s vs. %s' % (player_1_gfwl, player_2_gfwl))


command_pending.commands = ['pending']
command_pending.priority = 'medium'


def command_update(willie, trigger):

      PLAYER1, PLAYER2, TIE = range(3)
      args = trigger.group().split()

      try:
         match_code = args[1]
         player1_score = args[2]
         player2_score = args[3]
      except IndexError:
         willie.say('Invalid number of arguments.')
         return

      if player1_score > player2_score:
         winner = PLAYER1

      elif player2_score > player1_score:
         winner = PLAYER2

      else:
         winner = TIE

      match_list = challonge.matches.index(tournament_id)
      match_dict = {}
      ident_to_id = {}
      for match in match_list:
         ident_to_id[match['identifier']] = match['id']
         match_dict[match['id']] = match
      if match_code not in ident_to_id.keys():
         willie.say('Invalid match code.')

      match_id = ident_to_id[match_code]
      score_csv = '%s-%s' % (player1_score, player2_score)
      if winner == PLAYER1:
         winner_id = match_dict[match_id]['player1-id']
      elif winner == PLAYER2:
         winner_id = match_dict[match_id]['player2-id']
      else:
         winner_id = 'tie'
      willie.say('Reporting score...')
      challonge.matches.update(tournament_id, match_id, scores_csv=score_csv, winner_id=winner_id)
      willie.say('Finished.')


command_update.commands = ['update']
command_update.priority = 'medium'


def command_checkin(willie, trigger):

   args = trigger.group().split()
   try:
      bracket_name = args[1]
   except IndexError:
      willie.say('Bracket name not given.')
      return

   if bracket_name not in participants.keys():
      willie.say('No-one exists in the tournament under "%s"' % bracket_name)
      return
      
   try:
      username = args[2]
   except IndexError:
      username = trigger.nick
   gfwl_ids[bracket_name] = username

   willie.say('%s (GFWL ID %s) checked in' % (trigger.nick, username))


def command_rollcall(willie, trigger):

   if trigger.owner is False:
      willie.say('You can\'t tell me what to do!')
      return

   missing_users = set(particpants.iterkeys()) - set(gfwl_ids.iterkeys())
   if len(missing_users) == 0:
      willie.say('Everyone has checked in.')
      return

   willie.say('Missing users:')
   for user in missing_users:
      willie.say(user)
      

command_checkin.commands = ['checkin']
command_checkin.priority = 'medium'
