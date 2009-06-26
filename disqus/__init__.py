#:coding=utf8:

"""
disqus-api-client

A disqus api client for python.


"""

import simplejson
import httplib
import urllib

_debug = False

HOST = "disqus.com"
BASE_URL = "/api/%s/"

REQUEST_METHODS = {
    "create_post": "POST",
    "get_forum_list": "GET",
    "get_forum_api_key": "GET",
    "get_thread_list": "GET",
    "get_num_posts": "GET",
    "get_thread_by_url": "GET",
    "get_thread_posts": "GET",
    "thread_by_identiier": "POST",
    "update_thread": "POST",
}

class DisqusService(object):
    def login(self, api_key):
        self.api_key = api_key

    def create_post(self, **kwargs):
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

    def get_forum_list(self):
        """
        Key: User Key
        Arguments: None.
        
        Result: A list of objects representing all forums the user owns. The
                user is determined by the API key. See "Object Formats" header
                below for details on forum objects. 
        """
        resp = self._http_request("get_forum_list", key_required=True)
        return [decode_forum(f) for f in resp["message"]]

    def get_forum_api_key(self):
        """
        Key: User Key
        Arguments: "forum_id", the unique id of the forum.

        Result: A string which is the Forum Key for the given forum. 
        """
        pass

    def get_thread_list(self):
        """
        Key: Forum Key
        Arguments: None.
        
        Result: A list of objects representing all threads belonging to the
                given forum. See "Object Formats" for details on thread
                objects.
        """
        pass

    def get_num_posts(self, thread_ids):
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

    def get_thread_by_url(self, url):
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

    def get_thread_posts(self, thread_id):
        """
        Key: Forum Key
        Arguments: "thread_id": the ID of a thread belonging to the given 
                                forum.

        Result: A list of objects representing all posts belonging to the
                given forum. See "Object Formats" for details on post objects. 
        """
        pass

    def thread_by_identifier(self, title, identifier):
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

    def update_thread(self, **kwargs):
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

    def _http_request(self, method_name, data={}, key_required=False):
        if key_required:
            if not getattr(self, "api_key"):
                raise Exception("Please login")
            data["user_api_key"] = self.api_key

        method = REQUEST_METHODS[method_name]

        url = (BASE_URL +"?%s") % (method_name, urllib.urlencode(data))
        
        con = httplib.HTTPConnection(HOST)
        con.request(method, url)
        
        return simplejson.load(con.getresponse())

class Forum(object):
    """
    id field: a unique alphanumeric string identifying this Forum object.
    shortname: the unique string used in disqus.com URLs relating to this
               forum. For example, if the shortname is "bmb", the forum's
               community page is at http://bmb.disqus.com/.
    name: a string for displaying the forum's full title,
          like "The Eyeball Kid's Blog". 
    """
    def __init__(self, id, shortname, name):
        self.id = id
        self.shortname = shortname
        self.name = name

class Thread(object):
    """
    id: a unique alphanumeric string identifying this Thread object.
    forum: the id for the forum this thread belongs to.
    slug: the per-forum-unique string used for identifying this thread in
          disqus.com URLs relating to this thread. Composed of
          underscore-separated alphanumeric strings.
    title: the title of the thread.
    created_at: the UTC date this thread was created, in the format
                %Y-%m-%dT%H:%M.
    allow_comments: whether this thread is open to new comments.
    url: the URL this thread is on, if known.
    identifier: the user-provided identifier for this thread, as in
                thread_by_identifier above (if available) 
    """
    def __init__(self,
                 id,
                 forum,
                 slug,
                 title,
                 created_at,
                 allow_comments,
                 url,
                 identifier):
        self.id = id
        self.forum = forum
        self.slug = slug
        self.title = title
        self.created_at = created_at
        self.allow_comments = allow_comments
        self.url = url
        self.identifier = identifier

class Post(object):
    def __init__(self,
                 id,
                 forum,
                 thread,
                 created_at,
                 message,
                 parent_post,
                 shown,
                 is_anonymous=False,
                 anonymous_author=None,
                 author=None):
        """
        id: a unique alphanumeric string identifying this Post object.
        forum: the id for the forum this post belongs to.
        thread: the id for the thread this post belongs to.
        created_at: the UTC date this post was created, in the format %Y-%m-%dT%H:%M.
        message: the contents of the post, such as "First post".
        parent_post: the id of the parent post, if any
        shown: whether the post is currently visible or not.
        is_anonymous: whether the comment was left anonymously, as opposed to a
                      registered Disqus account.
        anonymous_author: An AnoymousAuthor object. Present only when is_anonymous is true. 
        author: Author object. Present only when is_anonymous is false. An object containing these fields:
                
        """
        self.id = id
        self.forum = forum
        self.thread = thread
        self.created_at = created_at
        self.message = message
        self.parent_post = parent_post
        self.shown = shown
        self.is_anonymous = is_anonymous
        if self.is_anoymous:
            self.anonymous_author = anonymous_author
            self.author = None
        else:
            self.author = author
            self.anonymous_author = None

class Author(object):
    def __init__(self,
                 id,
                 username,
                 display_name,
                 url,
                 email_hash,
                 has_avatar):
        """
        id: the unique id of the commenter's Disqus account
        username: the author's username
        display_name: the author's full name, if provided
        url: their optionally provided homepage
        email_hash: md5 of the author's email address
        has_avatar: whether the user has an avatar on disqus.com
        """
        self.id = id
        self.username = username
        self.display_name = display_name
        self.url = url
        self.email_hash = email_hash
        self.has_avatar = has_avatar

class AnonymousAuthor(object):
    def __init__(self,
                 name,
                 url,
                 email_hash):
        """
        name: the display name of the commenter
        url: their optionally provided homepage
        email_hash: md5 of the author's email address
        """
        self.name = name
        self.url = url
        self.email_hash = email_hash

def decode_response(dct):
    if dct.get("code") == "ok" and dct.get("succeeded"):
        return dct.get("message")
    else:
        #TODO: raise Proper exception
        raise Exception("%s: %s" % (dct.get("code"), dct.get("message")))

def decode_forum(dct):
    if _debug:
        print "decode_forum: %r" % dct
    return Forum(
        id=dct.get("id"),
        shortname=dct.get("shortname"),
        name=dct.get("name"),
    )

def decode_thread(dct):
    if _debug:
        print "decode_thread: %r" % dct
    return Thread(
        id=dct.get("id"),
        forum=dct.get("forum"),
        slug=dct.get("slug"),
        title=dct.get("title"),
        created_at=dct.get("created_at"),
        allow_comments=dct.get("allow_comments"),
        url=dct.get("url"),
        identifier=dct.get("identifier"),
    )

def decode_post(dct):
    if _debug:
        print "decode_post: %r" % dct
    return Post(
        id=dct.get("id"),
        forum=dtt.get("forum"),
        thread=dct.get("thread"),
        created_at=dct.get("created_at"),
        message=dct.get("message"),
        parent_post=dct.get("parent_post"),
        shown=dct.get("shown"),
        is_anonymous=dct.get("is_anonymous"),
        anonymous_author=dct.get("anonymous_author"),
        author=dct.get("author"),
    )

def decode_author(dct):
    if _debug:
        print "decode_author: %r" % dct
    return Author(
        id=dct.get("id"),
        username=dct.get("username"),
        display_name=dct.get("display_name"),
        url=dct.get("url"),
        email_hash=dct.get("email_hash"),
        has_avatar=dct.get("has_avatar"),
    )

def decode_anonymous_author(dct):
    if _debug:
        print "decode_anonymous_author: %r" % dct
    return AnonymousAuthor(
        name=dct["name"],
        url=dct["url"],
        email_hash=dct["email_hash"],
    )
