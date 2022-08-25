import React from 'react'
import { View,Text,StyleSheet } from 'react-native'

const HelloShrmaji = () => {
  return (
        <View style={styles.Card}>
            <Text>Hello Rohit Sharma!</Text>
        </View>
    )
}

const styles = StyleSheet.create({
    Card:{
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        fontSize: 23,
        borderRadius: 10,
        borderWidth: 1,
        borderColor: 'Grey'
    }
})

export default HelloWorld