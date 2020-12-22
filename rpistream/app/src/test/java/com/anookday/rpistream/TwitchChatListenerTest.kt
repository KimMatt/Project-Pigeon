package com.anookday.rpistream

import com.anookday.rpistream.chat.TwitchChatListener
import org.junit.Assert.assertEquals
import org.junit.Test

/**
 * Unit test for [TwitchChatListener].
 */
class TwitchChatListenerTest {
    private val listener = TwitchChatListener("authToken", "user") {}

    @Test
    fun testParseMessage() {
        val message = ":anotheruser!anotheruser@anotheruser.tmi.twitch.tv PRIVMSG #user :Kappa"
        assertEquals("anotheruser: Kappa", listener.parseMessage(message).toString())
    }
}