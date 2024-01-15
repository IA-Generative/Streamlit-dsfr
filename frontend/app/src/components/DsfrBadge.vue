<script setup lang="ts">
import { reactive } from 'vue'
import { DsfrBadge } from '@gouvminint/vue-dsfr'

import { useStreamlit } from '../streamlit'
import type { ComponentProps } from '../types/ComponentProps.d.ts'

useStreamlit()

const props = defineProps<
	ComponentProps<{
		small?: boolean
		type?: 'error' | 'success' | 'new' | 'info' | 'warning'
		label?: string
		noIcon?: boolean
		ellipsis?: boolean
	}>
>()
</script>

<template>
	<div class="component">
		<DsfrBadge v-bind="props.args" />
	</div>
</template>
