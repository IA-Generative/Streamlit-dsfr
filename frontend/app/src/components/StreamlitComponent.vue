<script setup lang="ts">
import type { Component } from 'vue'

import WithStreamlitConnection from '../streamlit/WithStreamlitConnection.vue'

const props = defineProps<{
	component: Component
}>()
</script>

<template>
	<WithStreamlitConnection v-slot="{ width, args, disabled, theme }">
		<component :is="props.component" :width="width" :args="args" :disabled="disabled" :theme="theme" />
	</WithStreamlitConnection>
</template>
