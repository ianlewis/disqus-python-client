#:coding=utf8:

"""
disqus-api-client

A disqus api client for python.


"""

import simplejson

class DisqusService(object):
    def login(api_key):
        self.api_key = api_key

    def create_post(**kwargs):
        """
        Key: Forum Key
        Method: POST
        Arguments: 
            Required: 
                "thread_id": the thread to post to
                "message": the content of the post
                "author_name": the post creator's name
                "author_email": their email address.
            Optional:
                "parent_post": the id of the parent post
                "created_at": the UTC date this post was created in the format
                              %Y-%m-%dT%H:%M (the current time will be used by
                              default)
                "author_url": the author's homepage; and "ip_address", their 
                              IP address.
        
        Action: Creates a new post on the thread. Does not check against spam
                filters or ban list. This is intended to allow automated
                importing of comments.
        
        Result: The post object just created. See "Object Formats" header below
                for details on post objects. 
        """
        pass

    def get_forum_list():
        """
        Key: User Key
        Arguments: None.
        
        Result: A list of objects representing all forums the user owns. The
                user is determined by the API key. See "Object Formats" header
                below for details on forum objects. 
        """
        pass

    def get_forum_api_key():
        """
        Key: User Key
        Arguments: "forum_id", the unique id of the forum.

        Result: A string which is the Forum Key for the given forum. 
        """
        pass

    def get_thread_list():
        """
        Key: Forum Key
        Arguments: None.
        
        Result: A list of objects representing all threads belonging to the
                given forum. See "Object Formats" for details on thread
                objects.
        """
        pass

    def get_num_posts(thread_ids):
        """
        Key: Forum Key
        Arguments: "thread_ids": a comma-separated list of thread IDs belonging
                                 to the given forum.

        Result: An object mapping each thread_id to a list of two numbers. The 
                first number is the number of visible comments on on the
                thread; this would be useful for showing users of the site
                (e.g., "5 Comments"). The second number is the total number of 
                comments on the thread. These numbers are different because
                some forums require moderator approval, some messages are
                flagged as spam, etc. 
        """
        pass

    def get_thread_by_url(url):
        """
        Key: Forum Key
        Arguments: "url", the URL to check for an associated thread.

        Result: A thread object if one was found, otherwise null. Only finds
                threads associated with the given forum. Note that there is
                no one-to-one mapping between threads and URLs: a thread will
                only have an associated URL if it was automatically created by
                Disqus javascript embedded on that page. Therefore, we
                recommend using thread_by_identifier whenever possible, and
                this method is provided mainly for handling comments from
                before your forum was using the API.
        """
        pass

    def get_thread_posts(thread_id):
        """
        Key: Forum Key
        Arguments: "thread_id": the ID of a thread belonging to the given 
                                forum.

        Result: A list of objects representing all posts belonging to the
                given forum. See "Object Formats" for details on post objects. 
        """
        pass

    def thread_by_identifier(title, identifier):
        """
        Key: Forum Key
        Method: POST
        Arguments: "title": the title of the thread to possibly be created
                   "identifier": a string of your choosing (see Action).

        Action: Create or retrieve a thread by an arbitrary identifying string
                of your choice. For example, you could use your local
                database's ID for the thread. This method allows you to
                decouple thread identifiers from the URLs on which they might
                be appear. (Disqus would normally use a thread's URL to
                identify it, which is problematic when URLs do not uniquely 
                identify a resource.) If no thread yet exists for the given
                identifier (paired with the forum), one will be created.

        Result: An object with two keys:
                    "thread": which is the thread object corresponding to the
                              identifier
                    "created": which indicates whether the thread was created
                               as a result of this method call. If created, it
                               will have the specified title. 
        """
        pass

    def update_thread(**kwargs):
        """
        Key: Forum Key
        Method: POST
        Arguments: 
            Required: 
                "thread_id": the ID of a thread belonging to the given forum.
            Optional: 
                any of "title", "slug", "url", and "allow_comments".
        
        Action: Sets the provided values on the thread object. See Object
                Formats for field meanings.
        
        Result: An empty success message. 
        """
        pass
