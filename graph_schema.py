# Do not edit! Generated automatically by mockfacebook.
# http://code.google.com/p/mockfacebook/
# 2011-11-08 15:42:26.765861

{'connections': {u'album': [u'photos', u'likes', u'comments'],
                 u'application': [u'feed',
                                  u'picture',
                                  u'tagged',
                                  u'videos',
                                  u'links',
                                  u'subscriptions',
                                  u'notes',
                                  u'posts',
                                  u'photos',
                                  u'albums',
                                  u'events',
                                  u'statuses',
                                  u'insights'],
                 u'checkin': [u'likes', u'comments'],
                 u'comment': [u'likes', u'comments'],
                 u'event': [u'feed',
                            u'picture',
                            u'noreply',
                            u'maybe',
                            u'invited',
                            u'attending',
                            u'declined'],
                 u'friendlist': [u'members'],
                 u'group': [u'feed', u'picture', u'members', u'docs'],
                 u'link': [u'likes', u'comments'],
                 u'note': [u'comments'],
                 u'page': [u'feed',
                           u'tagged',
                           u'videos',
                           u'links',
                           u'notes',
                           u'posts',
                           u'photos',
                           u'questions',
                           u'albums',
                           u'events',
                           u'statuses'],
                 u'photo': [u'likes', u'comments'],
                 u'status': [u'likes', u'comments'],
                 u'user': [u'feed',
                           u'tagged',
                           u'family',
                           u'picture',
                           u'mutualfriends',
                           u'books',
                           u'accounts',
                           u'likes',
                           u'home',
                           u'statuses',
                           u'friendrequests',
                           u'links',
                           u'checkins',
                           u'music',
                           u'videos',
                           u'events',
                           u'adaccounts',
                           u'interests',
                           u'activities',
                           u'apprequests',
                           u'photos',
                           u'updates',
                           u'groups',
                           u'scores',
                           u'friendlists',
                           u'outbox',
                           u'albums',
                           u'friends',
                           u'permissions',
                           u'television',
                           u'notifications',
                           u'notes',
                           u'posts',
                           u'movies',
                           u'games',
                           u'payments',
                           u'inbox'],
                 u'video': [u'likes', u'comments']},
 'tables': {u'album': [Column(name=u'id', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'from', fb_type='object', sqlite_type='', indexable=None),
                       Column(name=u'name', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'description', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'location', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'link', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'cover_photo', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'privacy', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'count', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'type', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'created_time', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'updated_time', fb_type='string', sqlite_type='TEXT', indexable=None)],
            u'application': [Column(name=u'id', fb_type='string', sqlite_type='TEXT', indexable=None),
                             Column(name=u'name', fb_type='string', sqlite_type='TEXT', indexable=None),
                             Column(name=u'description', fb_type='string', sqlite_type='TEXT', indexable=None),
                             Column(name=u'canvas_name', fb_type='string', sqlite_type='TEXT', indexable=None),
                             Column(name=u'category', fb_type='string', sqlite_type='TEXT', indexable=None),
                             Column(name=u'company', fb_type='string', sqlite_type='TEXT', indexable=None),
                             Column(name=u'icon_url', fb_type='string', sqlite_type='TEXT', indexable=None),
                             Column(name=u'subcategory', fb_type='string', sqlite_type='TEXT', indexable=None),
                             Column(name=u'link', fb_type='string', sqlite_type='TEXT', indexable=None),
                             Column(name=u'logo_url', fb_type='string', sqlite_type='TEXT', indexable=None),
                             Column(name=u'daily_active_users', fb_type='string', sqlite_type='TEXT', indexable=None),
                             Column(name=u'weekly_active_users', fb_type='string', sqlite_type='TEXT', indexable=None),
                             Column(name=u'monthly_active_users', fb_type='string', sqlite_type='TEXT', indexable=None),
                             Column(name=u'migrations', fb_type='array', sqlite_type='', indexable=None),
                             Column(name=u'namespace', fb_type='string', sqlite_type='TEXT', indexable=None),
                             Column(name=u'restrictions', fb_type='object', sqlite_type='', indexable=None)],
            u'checkin': [Column(name=u'id', fb_type='string', sqlite_type='TEXT', indexable=None),
                         Column(name=u'from', fb_type='object', sqlite_type='', indexable=None),
                         Column(name=u'tags', fb_type='array', sqlite_type='', indexable=None),
                         Column(name=u'place', fb_type='object', sqlite_type='', indexable=None),
                         Column(name=u'application', fb_type='object', sqlite_type='', indexable=None),
                         Column(name=u'created_time', fb_type='string', sqlite_type='TEXT', indexable=None),
                         Column(name=u'likes', fb_type='array', sqlite_type='', indexable=None),
                         Column(name=u'message', fb_type='string', sqlite_type='TEXT', indexable=None),
                         Column(name=u'comments', fb_type='array', sqlite_type='', indexable=None),
                         Column(name=u'type', fb_type='string', sqlite_type='TEXT', indexable=None)],
            u'comment': [Column(name=u'id', fb_type='string', sqlite_type='TEXT', indexable=None),
                         Column(name=u'from', fb_type='object', sqlite_type='', indexable=None),
                         Column(name=u'message', fb_type='string', sqlite_type='TEXT', indexable=None),
                         Column(name=u'created_time', fb_type='string', sqlite_type='TEXT', indexable=None),
                         Column(name=u'likes', fb_type='int', sqlite_type='INTEGER', indexable=None),
                         Column(name=u'user_likes', fb_type='string', sqlite_type='TEXT', indexable=None),
                         Column(name=u'type', fb_type='string', sqlite_type='TEXT', indexable=None)],
            u'domain': [Column(name=u'id', fb_type='string', sqlite_type='TEXT', indexable=None),
                        Column(name=u'name', fb_type='string', sqlite_type='TEXT', indexable=None)],
            u'event': [Column(name=u'id', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'owner', fb_type='object', sqlite_type='', indexable=None),
                       Column(name=u'name', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'description', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'start_time', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'end_time', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'location', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'venue', fb_type='object', sqlite_type='', indexable=None),
                       Column(name=u'privacy', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'updated_time', fb_type='string', sqlite_type='TEXT', indexable=None)],
            u'friendlist': [Column(name=u'id', fb_type='string', sqlite_type='TEXT', indexable=None),
                            Column(name=u'name', fb_type='string', sqlite_type='TEXT', indexable=None),
                            Column(name=u'type', fb_type='string', sqlite_type='TEXT', indexable=None)],
            u'group': [Column(name=u'id', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'version', fb_type='int', sqlite_type='INTEGER', indexable=None),
                       Column(name=u'icon', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'owner', fb_type='object', sqlite_type='', indexable=None),
                       Column(name=u'name', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'description', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'link', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'privacy', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'updated_time', fb_type='string', sqlite_type='TEXT', indexable=None)],
            u'note': [Column(name=u'id', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'from', fb_type='object', sqlite_type='', indexable=None),
                      Column(name=u'subject', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'message', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'comments', fb_type='array', sqlite_type='', indexable=None),
                      Column(name=u'created_time', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'updated_time', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'icon', fb_type='string', sqlite_type='TEXT', indexable=None)],
            u'page': [Column(name=u'id', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'name', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'link', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'category', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'likes', fb_type='int', sqlite_type='INTEGER', indexable=None),
                      Column(name=u'location', fb_type='object', sqlite_type='', indexable=None),
                      Column(name=u'phone', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'checkins', fb_type='int', sqlite_type='INTEGER', indexable=None),
                      Column(name=u'access_token', fb_type='string', sqlite_type='TEXT', indexable=None)],
            u'photo': [Column(name=u'id', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'from', fb_type='object', sqlite_type='', indexable=None),
                       Column(name=u'tags', fb_type='array', sqlite_type='', indexable=None),
                       Column(name=u'name', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'icon', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'picture', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'source', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'height', fb_type='int', sqlite_type='INTEGER', indexable=None),
                       Column(name=u'width', fb_type='int', sqlite_type='INTEGER', indexable=None),
                       Column(name=u'images', fb_type='array', sqlite_type='', indexable=None),
                       Column(name=u'link', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'created_time', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'updated_time', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'position', fb_type='int', sqlite_type='INTEGER', indexable=None)],
            u'status': [Column(name=u'id', fb_type='string', sqlite_type='TEXT', indexable=None),
                        Column(name=u'from', fb_type='object', sqlite_type='', indexable=None),
                        Column(name=u'message', fb_type='string', sqlite_type='TEXT', indexable=None),
                        Column(name=u'updated_time', fb_type='string', sqlite_type='TEXT', indexable=None),
                        Column(name=u'type', fb_type='string', sqlite_type='TEXT', indexable=None)],
            u'user': [Column(name=u'id', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'name', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'first_name', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'middle_name', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'last_name', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'gender', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'locale', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'languages', fb_type='array', sqlite_type='', indexable=None),
                      Column(name=u'link', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'username', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'third_party_id', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'timezone', fb_type='int', sqlite_type='INTEGER', indexable=None),
                      Column(name=u'updated_time', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'verified', fb_type='bool', sqlite_type='INTEGER', indexable=None),
                      Column(name=u'bio', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'birthday', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'education', fb_type='array', sqlite_type='', indexable=None),
                      Column(name=u'email', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'hometown', fb_type='object', sqlite_type='', indexable=None),
                      Column(name=u'interested_in', fb_type='array', sqlite_type='', indexable=None),
                      Column(name=u'location', fb_type='object', sqlite_type='', indexable=None),
                      Column(name=u'political', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'favorite_athletes', fb_type='array', sqlite_type='', indexable=None),
                      Column(name=u'favorite_teams', fb_type='array', sqlite_type='', indexable=None),
                      Column(name=u'quotes', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'relationship_status', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'religion', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'significant_other', fb_type='object', sqlite_type='', indexable=None),
                      Column(name=u'video_upload_limits', fb_type='object', sqlite_type='', indexable=None),
                      Column(name=u'website', fb_type='string', sqlite_type='TEXT', indexable=None),
                      Column(name=u'work', fb_type='array', sqlite_type='', indexable=None)],
            u'video': [Column(name=u'id', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'from', fb_type='object', sqlite_type='', indexable=None),
                       Column(name=u'tags', fb_type='array', sqlite_type='', indexable=None),
                       Column(name=u'name', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'description', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'picture', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'embed_html', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'icon', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'source', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'created_time', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'updated_time', fb_type='string', sqlite_type='TEXT', indexable=None),
                       Column(name=u'comments', fb_type='array', sqlite_type='', indexable=None)]}}
