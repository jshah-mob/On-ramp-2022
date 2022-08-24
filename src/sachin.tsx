import React from 'react';
import {Modal, SafeAreaView, View} from 'react-native';
import {FlatListView} from './FlatList';
import ModalView from './Modal';
import Parent from './parent';

const App = () => {
  return (
    <SafeAreaView>
      <View>
        <FlatListView />
      </View>
    </SafeAreaView>
  );
};

export default App;
